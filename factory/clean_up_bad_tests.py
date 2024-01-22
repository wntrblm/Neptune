from pathlib import Path
from wintertools.reportcard import Report

for reportfn in Path("./reports").glob("*.json"):
    report = Report.load(reportfn)

    if not report.succeeded:
        print(f"deleting {reportfn}")
        reportfn.unlink()

        for fn in Path("./measurements/").glob(f"{report.ulid}*"):
            print(f"deleting {fn}")
            fn.unlink()
