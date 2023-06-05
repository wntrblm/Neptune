from rich import print
from wintertools import reportcard, thermalprinter
from wintertools.multimeter import Multimeter

from hubble import Hubble

h = Hubble()

if __name__ == "__main__":
    report = reportcard.Report(
        name="?",
    )

    print(report)
    report.save()
    reportcard.render_html(report)

    if report.succeeded:
        h.success()
        print("PASSED")
    else:
        h.fail()
        print("FAILED")

    if report.succeeded:
        thermalprinter.print_me_maybe(reportcard.render_image(report))
