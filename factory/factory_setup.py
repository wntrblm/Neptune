from rich import print
from wintertools import reportcard, thermalprinter
from hubble import Hubble

from libneptune import NeptuneLens


hubble = Hubble()
lens = NeptuneLens(hubble)


def alt():
    lens.reset()
    lens.knob_tests_low_pass_fully_open()
    print("ok")


def main():
    report = reportcard.Report(
        name="Neptune",
    )

    print(report)
    report.save()
    reportcard.render_html(report)

    if report.succeeded:
        hubble.success()
        print("PASSED")
    else:
        hubble.fail()
        print("FAILED")

    if report.succeeded:
        thermalprinter.print_me_maybe(reportcard.render_image(report))


if __name__ == "__main__":
    # main()
    alt()
