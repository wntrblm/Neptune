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

from libneptune import NeptuneLens


MEASUREMENTS = {
    "knob-lp-open": dict(
        name="Knobs: Low pass open",
        fn="knob_tests_low_pass_fully_open",
        strategy="passfail",
    ),
    "knob-lp-center": dict(
        name="Knobs: Low pass center",
        fn="knob_tests_low_pass_centered",
        strategy="passfail",
    ),
    "knob-lp-closed": dict(
        name="Knobs: Low pass closed",
        fn="knob_tests_low_pass_fully_closed",
        strategy="passfail",
    ),
    "knob-lp-reso": dict(
        name="Knobs: Resonant low pass",
        fn="knob_tests_resonant_low_pass",
        strategy="passfail",
    ),
    "knob-lp-salt": dict(
        name="Knobs: Salty low pass",
        fn="knob_tests_salty_low_pass",
        strategy="passfail",
    ),
    "knob-hp-open": dict(
        name="Knobs: High pass open",
        fn="knob_tests_high_pass_fully_open",
        strategy="passfail",
    ),
    "knob-hp-center": dict(
        name="Knobs: High pass center",
        fn="knob_tests_high_pass_centered",
        strategy="passfail",
    ),
    "knob-hp-closed": dict(
        name="Knobs: High pass closed",
        fn="knob_tests_high_pass_fully_closed",
        strategy="passfail",
    ),
    "knob-self-osc": dict(
        name="Knobs: Self oscillation",
        fn="knob_tests_self_oscillation",
        strategy="selfosc",
    ),
    "cv-fm1-pos": dict(
        name="CV: FM1 full",
        fn="cv_tests_fm1_full",
        strategy="passfail",
    ),
    "cv-fm1-neg": dict(
        name="CV: FM1 inversion",
        fn="cv_tests_fm1_full_inversion",
        strategy="passfail",
    ),
    "cv-fm2-open": dict(
        name="CV: FM2 open",
        fn="cv_tests_fm2_fully_open",
        strategy="passfail",
    ),
    "cv-lp-reso": dict(
        name="CV: Resonant low pass",
        fn="cv_tests_resonant_low_pass",
        strategy="passfail",
    ),
    "cv-lp-salt": dict(
        name="CV: Salty low pass",
        fn="cv_tests_salty_low_pass",
        strategy="passfail",
    ),
    "cv-vol": dict(
        name="CV: Vol VCA",
        fn="cv_tests_vol_vca",
        strategy="passfail",
    ),
    "cv-self-osc": dict(
        name="CV: Self oscillation",
        fn="cv_tests_self_oscillation",
        strategy="selfosc",
    ),
}


def setup_scope(scope: oscilloscope.Oscilloscope):
    scope.enable_bandwidth_limit()
    scope.enable_channel("c1")
    scope.set_vertical_division("c1", "4V")
    scope.set_vertical_offset("c1", "0V")
    scope.set_time_division("200us")


def take_measurements(
    *,
    scope: oscilloscope.Oscilloscope,
    lens: NeptuneLens,
    wait_time=0.4,
    step=1000,
) -> dict[str, waveform.Waveform]:
    lens.reset()

    results = {}

    for mkey, m in MEASUREMENTS.items():
        getattr(lens, m["fn"])()

        time.sleep(wait_time)

        wf = scope.get_waveform("c1", step=step)

        results[mkey] = wf
        print(f"✓ Measured {m['name']}")

    return results


def save_measurements(id: str, measurements):
    dstdir = Path("./measurements")
    dstdir.mkdir(exist_ok=True)

    for key, wf in measurements.items():
        dst = dstdir / f"{id}-{key}.json"
        wf.save(dst)
        print(f"✓ Saved {dst}")


def load_measurements(id: str):
    results = {}
    dstdir = Path("./measurements")

    for key in MEASUREMENTS.keys():
        dst = dstdir / f"{id}-{key}.json"
        wf = waveform.Waveform.load(dst)
        results[key] = wf
        print(f"✓ Loaded {dst}")

    return results


def check_measurements(measurements: dict[str, waveform.Waveform]):
    results = {}

    for key, wf in measurements.items():
        name = MEASUREMENTS[key]["name"]
        strategy = MEASUREMENTS[key]["strategy"]

        passed = False
        details = ""

        if strategy == "passfail":
            passfail = waveform.WaveformPassFail.load_from_image(
                f"./references/{key}.png"
            )

            result = passfail.compare(wf)

            result.composite_image.save(f"./{key}.png")

            passed = result.pass_ratio > 0.9
            details = f"{result.pass_ratio * 100:.0f}%"

        elif strategy == "selfosc":
            # Just check frequency and amplitude
            passed = (
                wf.frequency > 100 and wf.frequency < 20_000 and wf.voltage_span > 5
            )

        if passed:
            print(f"✓ {name}: {details}")
        else:
            print(f"!! {name}: {details}")

        results[key] = reportcard.PassFailItem(
            label=name, value=passed, details=details
        )

    return results


def waveform_to_linegraphitem(wf, *, points=200, stroke="black", stroke_width=8):
    return reportcard.LineGraphItem(
        series=[
            reportcard.Series(
                data=wf.to_list(points),
                stroke=stroke,
                stroke_width=stroke_width,
            ),
        ],
        graph=reportcard.LineGraph.from_waveform(wf),
    )


BLACKISH = "#231F20"
TEALS = (
    "#99D1D6",
    "#66ADB5",
    "#408C94",
    "#267880",
)
REDS = (
    "#F597A3",
    "#F2727F",
    "#DB475B",
    "#C02435",
)
PURPLES = (
    "#C7B8ED",
    "#A38AD6",
    "#7D61BA",
    "#5E409E",
)
COLORS = np.array([TEALS, REDS, PURPLES]).T.flatten()
DEFAULT_STROKES = (BLACKISH, TEALS[-1], REDS[-1], PURPLES[-1])


def waveforms_to_linegraphitem(
    wfs, *, points=200, strokes=DEFAULT_STROKES, stroke_width=4
):
    return reportcard.LineGraphItem(
        series=[
            reportcard.Series(
                data=wf.to_list(points),
                stroke=strokes[n % len(strokes)],
                stroke_width=stroke_width,
            )
            for n, wf in enumerate(wfs)
        ],
        graph=reportcard.LineGraph.from_waveform(wfs[0], label=""),
    )


def create_references():
    measurements_dir = Path("./measurements")

    for key in MEASUREMENTS.keys():
        passfail = waveform.WaveformPassFail()

        wf_files = measurements_dir.glob(f"*-{key}.json")

        for wf_file in wf_files:
            wf = waveform.Waveform.load(wf_file)
            passfail.add_reference(wf, tolerance=0.02)

        dst = f"references/{key}.png"
        passfail.save_as_image(dst)

        print(f"✓ Created {dst}")


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--create-references",
        action="store_true",
        help="Create reference masks from existing data.",
    )
    parser.add_argument(
        "--existing",
        type=str,
        help="Load existing measurements for the given ULID",
    )
    parser.add_argument(
        "--reprint",
        action="store_true",
        help="Reprint existing",
    )
    parser.add_argument("--style", choices=["full", "brief"], default="brief")

    args = parser.parse_args()

    if args.create_references:
        print("# Creating waveform references")
        return create_references()

    report = reportcard.Report(
        name="Neptune",
    )

    if args.existing:
        report.ulid = args.existing

    hubble = None
    measurements = None

    if not args.existing:
        hubble = Hubble()
        lens = NeptuneLens(hubble)
        scope = oscilloscope.Oscilloscope()

        print("# Configuring scope")
        setup_scope(scope)

        print("# Taking measurements")
        lens.reset()

        measurements = take_measurements(scope=scope, lens=lens)

        print("# Saving measurements")

    else:
        print("# Loading measurements")
        measurements = load_measurements(args.existing)

    print("# Checking waveforms")

    results = check_measurements(measurements)

    print("# Creating report")

    waveform_section = reportcard.Section(name="Waveforms")

    if args.style == "full":
        for key, wf in measurements.items():
            waveform_section.items.append(results[key])
            waveform_section.items.append(waveform_to_linegraphitem(wf))
    else:
        lp = (
            measurements["knob-lp-open"],
            measurements["knob-lp-center"],
            measurements["knob-lp-closed"],
            measurements["knob-lp-reso"],
            measurements["knob-lp-salt"],
        )
        report.sections.append(
            reportcard.Section(
                name="Low Pass",
                items=[waveforms_to_linegraphitem(lp, stroke_width=6)],
            )
        )
        hp = (
            measurements["knob-hp-open"],
            measurements["knob-hp-center"],
            measurements["knob-hp-closed"],
        )
        report.sections.append(
            reportcard.Section(
                name="High Pass",
                items=[waveforms_to_linegraphitem(hp, stroke_width=6)],
            )
        )
        selfosc = (
            measurements["knob-self-osc"],
            measurements["cv-self-osc"],
        )
        report.sections.append(
            reportcard.Section(
                name="Self Osc",
                items=[waveforms_to_linegraphitem(selfosc, stroke_width=6)],
            )
        )

        for key, wf in measurements.items():
            waveform_section.items.append(results[key])

    report.sections.append(waveform_section)

    print(report)

    if report.succeeded:
        print("PASSED")
        if hubble:
            hubble.success()
    else:
        report.ulid = "failed"
        print("FAILED")
        if hubble:
            hubble.fail()

    save_measurements(id=report.ulid, measurements=measurements)
    report.save()
    reportcard.render_html(report)

    if (not args.existing or args.reprint) and report.succeeded:
        report_image = reportcard.render_image(report)
        thermalprinter.print_me_maybe(report_image)


if __name__ == "__main__":
    main()
