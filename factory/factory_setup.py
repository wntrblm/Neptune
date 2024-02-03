# Copyright (c) 2024 Alethea Katherine Flowers.
# Published under the standard MIT License.
# Full text available at: https://opensource.org/licenses/MIT

import argparse
from pathlib import Path
import time

import numpy as np
from wintertools import reportcard, thermalprinter, oscilloscope, waveform
from wintertools.print import print
from hubble import Hubble

from libneptune import NeptuneLens, CW

WAVEFORM_TESTS = {
    "knob-lp-open": dict(
        label="Knobs: Low pass open",
        fn="knob_tests_low_pass_fully_open",
    ),
    "knob-lp-center": dict(
        label="Knobs: Low pass center",
        fn="knob_tests_low_pass_centered",
    ),
    "knob-lp-closed": dict(
        label="Knobs: Low pass closed",
        fn="knob_tests_low_pass_fully_closed",
    ),
    "knob-hp-open": dict(
        label="Knobs: High pass open",
        fn="knob_tests_high_pass_fully_open",
    ),
    "knob-hp-center": dict(
        label="Knobs: High pass center",
        fn="knob_tests_high_pass_centered",
    ),
    "knob-hp-closed": dict(
        label="Knobs: High pass closed",
        fn="knob_tests_high_pass_fully_closed",
    ),
    "cv-fm1-pos": dict(
        label="CV: FM1 full",
        fn="cv_tests_fm1_full",
    ),
    "cv-fm1-neg": dict(
        label="CV: FM1 inversion",
        fn="cv_tests_fm1_full_inversion",
    ),
    "cv-fm2-open": dict(
        label="CV: FM2 open",
        fn="cv_tests_fm2_fully_open",
    ),
    "cv-vol": dict(
        label="CV: Vol VCA",
        fn="cv_tests_vol_vca",
    ),
}
WAVEFORM_STEP = 1000

# This is the maximum allowed DC offset for a filter to "pass" testing. Due to
# the input offset voltage of the TL074s we used, the overall DC offset can
# be significant, but anything under this amount is considered within spec.
MAX_DC_OFFSET = 2

# These control how self-oscillation and salt are tested.
# Used to check that self-oscillation is happening and is appropriately loud and
# within the right frequency range.
SELF_OSC_MIN_AMPLITUDE = 6
SELF_OSC_MIN_FREQUENCY = 500
SELF_OSC_MAX_FREQUENCY = 3_000
# U used to make sure salt has the appropriate impact on resonance.
SELF_OSC_SALT_MIN_ATTENUATION = 0.75


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--create-references",
        action="store_true",
        help="Create reference pass/fail masks from existing data.",
    )

    args = parser.parse_args()

    if args.create_references:
        return create_waveform_references()

    report = reportcard.Report(
        name="Neptune",
    )

    hubble = Hubble()

    run_tests(hubble=hubble, report=report)

    reportcard.render_html(report)

    if report.succeeded:
        report_image = reportcard.render_image(report)
        thermalprinter.print_me_maybe(report_image)


def run_tests(*, hubble: Hubble, report: reportcard.Report):
    tests_section = reportcard.Section(name="Tests")
    report.append(tests_section)

    lens = NeptuneLens(hubble)
    scope = oscilloscope.Oscilloscope()
    lens.reset()

    print("# Configuring scope")
    setup_scope(scope)

    print("# Measuring DC offset")
    tests_section.append(test_dc_offset(scope=scope))

    if not tests_section.succeeded:
        report.ulid = "failed"
        return False

    print("# Checking reso & salt")
    reso_section = test_reso_and_salt(scope=scope, lens=lens)
    report.sections.insert(1, reso_section)

    if not reso_section.succeeded:
        report.ulid = "failed"
        return False

    print("# Checking waveforms")

    wf_measurements, wf_results = test_waveforms(scope=scope, lens=lens)

    tests_section.extend(wf_results)
    if report.succeeded:
        report.sections.insert(
            0,
            reportcard.Section(
                name="Waveforms",
                items=create_combined_waveform_graphs(wf_measurements),
            ),
        )

    # Done, report results

    if report.succeeded:
        hubble.success()
    else:
        report.ulid = "failed"
        hubble.fail()

    save_waveform_measurements(id=report.ulid, measurements=wf_measurements)
    report.save()

    return report.succeeded


###############################################################################
# Test methods
###############################################################################


def setup_scope(scope: oscilloscope.Oscilloscope):
    scope.enable_bandwidth_limit()
    scope.enable_channel("c1")
    scope.set_vertical_division("c1", "4V")
    scope.set_vertical_offset("c1", "0V")
    scope.set_time_division("200us")
    scope.set_trigger_level("c1", "0V")


def test_dc_offset(scope: oscilloscope.Oscilloscope) -> reportcard.PassFailItem:
    """Measures and checks the overall DC offset of the filter."""
    scope.set_dc_coupling("c1")
    time.sleep(0.5)

    offset = scope.get_mean("c1")

    scope.set_ac_coupling("c1")
    time.sleep(0.5)

    passed = abs(offset) < MAX_DC_OFFSET

    result = reportcard.PassFailItem(
        label="DC offset",
        value=passed,
        details=f"{offset:0.2f}V",
    )

    print(result)
    return result


def test_reso_and_salt(
    *, lens: NeptuneLens, scope: oscilloscope.Oscilloscope
) -> reportcard.Section:
    """Tests both resonant self-oscillation and salt.

    We used a interesting technique here that plays on the relationship between
    resonance and salt. First, we put the filter just over the threshold of
    self-oscillation and check that there's a proper waveform. We then apply
    salt which has the side-effect of attenuating self-oscillation. We can use
    measure the amount of attentuation to validate salt.

    One of the major reasons for using this technique over adding salt to other
    tests is that it's difficult to see the impact of resonance and salt when
    the input waveform volume is all the way up.
    """
    section = reportcard.Section(name="Reso & salt")

    # Check basic self-oscillation
    lens.cv_tests_self_oscillation()

    time.sleep(1)
    wf = scope.get_waveform("c1", WAVEFORM_STEP)

    section.append(reportcard.LineGraphItem.from_waveform(wf, label="Self-oscillation"))
    print(
        section.append(
            reportcard.PassFailItem(
                label="Amplitude",
                value=wf.voltage_span > SELF_OSC_MIN_AMPLITUDE,
                details=f"{wf.voltage_span:0.2f}V",
            )
        )
    )
    print(
        section.append(
            reportcard.PassFailItem(
                label="Frequency",
                value=wf.frequency > SELF_OSC_MIN_FREQUENCY
                and wf.frequency < SELF_OSC_MAX_FREQUENCY,
                details=f"{wf.frequency:0.0f}Hz",
            )
        )
    )

    # Bail early
    if not section.succeeded:
        return section

    # Check salt's impact on resonance and self-oscillation. First with CV
    # alone and then with the knob.

    salt_cv_ampl = 0
    salt_cv_passed = False
    for n in np.linspace(2, 4, num=8):
        print(f"Trying {n:0.2f} V...")
        lens.salt_cv = n
        time.sleep(0.3)
        salt_cv_ampl = scope.get_peak_to_peak("c1")
        if salt_cv_ampl > 1 and salt_cv_ampl < wf.voltage_span * SELF_OSC_SALT_MIN_ATTENUATION:
            salt_cv_passed = True
            break

    print(
        section.append(
            reportcard.PassFailItem(
                label="Salt CV attenutation",
                value=salt_cv_passed,
                details=f"{salt_cv_ampl:0.2f}V",
            )
        )
    )

    # Bail early
    if not section.succeeded:
        return section

    # Now with the knob. We do a dumb trick here where we also send negative CV
    # to offset the knob so we can see the effect more consistently.
    lens.salt_cv = -4
    lens.salt_knob = CW

    time.sleep(1)
    salt_knob_ampl = scope.get_peak_to_peak("c1")


    salt_knob_ampl = 0
    salt_knob_passed = False
    for n in np.linspace(-4, -2, num=8):
        print(f"Trying {n:0.2f} V...")
        lens.salt_cv = n
        time.sleep(0.3)
        salt_knob_ampl = scope.get_peak_to_peak("c1")
        if salt_knob_ampl > 1 and salt_knob_ampl < wf.voltage_span * SELF_OSC_SALT_MIN_ATTENUATION:
            salt_knob_passed = True
            break

    print(
        section.append(
            reportcard.PassFailItem(
                label="Salt knob attenutation",
                value=salt_knob_passed,
                details=f"{salt_knob_ampl:0.2f}V",
            )
        )
    )

    return section


def test_waveforms(
    *, scope: oscilloscope.Oscilloscope, lens: NeptuneLens
) -> tuple[dict[str, waveform.Waveform], list[reportcard.PassFailItem]]:
    measurements = {}
    results = []

    for name, config in WAVEFORM_TESTS.items():
        wf = measurements[name] = measure_waveform(
            lens_fn=config["fn"],
            scope=scope,
            lens=lens,
            wait_time=0.4,
            step=WAVEFORM_STEP,
        )

        result = check_waveform(name=name, label=config["label"], wf=wf)

        print(result)
        results.append(result)

        # Bail early
        if not result.succeeded:
            break

    return measurements, results


###############################################################################
# Helpers
###############################################################################


def measure_waveform(
    *,
    lens_fn: str,
    scope: oscilloscope.Oscilloscope,
    lens: NeptuneLens,
    wait_time=0.8,
    step=WAVEFORM_STEP,
) -> waveform.Waveform:
    lens.reset()

    getattr(lens, lens_fn)()

    time.sleep(wait_time)
    wf = scope.get_waveform("c1", step=step)

    return wf


def check_waveform(*, name: str, label: str, wf: waveform.Waveform):
    passfail = waveform.WaveformPassFail.load_from_image(f"./references/{name}.png")

    result = passfail.compare(wf)
    passed = result.pass_ratio > 0.9
    details = f"{result.pass_ratio * 100:.0f}%"

    # Save image for debugging
    result.composite_image.save(f"./last/{name}.png")

    return reportcard.PassFailItem(label=label, value=passed, details=details)


def save_waveform_measurements(id: str, measurements):
    dstdir = Path("./measurements")
    dstdir.mkdir(exist_ok=True)

    for key, wf in measurements.items():
        dst = dstdir / f"{id}-{key}.json"
        wf.save(dst)
        print(f"✓ Saved {dst}")


def load_waveform_measurements(id: str):
    results = {}
    dstdir = Path("./measurements")

    for key in WAVEFORM_TESTS.keys():
        dst = dstdir / f"{id}-{key}.json"
        wf = waveform.Waveform.load(dst)
        results[key] = wf
        print(f"✓ Loaded {dst}")

    return results


def create_waveform_references():
    print("# Creating waveform references")
    measurements_dir = Path("./measurements")

    for key in WAVEFORM_TESTS.keys():
        passfail = waveform.WaveformPassFail()

        wf_files = measurements_dir.glob(f"*-{key}.json")

        for wf_file in wf_files:
            wf = waveform.Waveform.load(wf_file)
            passfail.add_reference(wf, tolerance=0.02)

        dst = f"references/{key}.png"
        passfail.save_as_image(dst)

        print(f"✓ Created {dst}")


def create_combined_waveform_graphs(measurements: dict[str, waveform.Waveform]):
    graphs = []
    lp = [
        measurements["knob-lp-open"],
        measurements["knob-lp-center"],
        measurements["knob-lp-closed"],
    ]
    graphs.append(
        reportcard.LineGraphItem.from_waveform(lp, label="Low pass", stroke_width=6),
    )
    hp = [
        measurements["knob-hp-open"],
        measurements["knob-hp-center"],
        measurements["knob-hp-closed"],
    ]
    graphs.append(
        reportcard.LineGraphItem.from_waveform(hp, label="High pass", stroke_width=6),
    )
    return graphs


###############################################################################
# Entry
###############################################################################


if __name__ == "__main__":
    main()
