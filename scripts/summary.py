"""Turn a pytest JUnit XML report into a Markdown table for $GITHUB_STEP_SUMMARY."""
import os
import sys
import xml.etree.ElementTree as ET

report = sys.argv[1] if len(sys.argv) > 1 else "report.xml"
suite = ET.parse(report).getroot()
if suite.tag == "testsuites":
    suite = suite[0]

lines = [
    f"## Test results (Python {sys.version.split()[0]})",
    "",
    "| Test | Result | Time (s) |",
    "| --- | --- | --- |",
]
for case in suite.iter("testcase"):
    failed = case.find("failure") is not None or case.find("error") is not None
    skipped = case.find("skipped") is not None
    result = "❌ failed" if failed else ("⏭️ skipped" if skipped else "✅ passed")
    lines.append(f"| {case.get('name')} | {result} | {float(case.get('time', 0)):.3f} |")

total = int(suite.get("tests", 0))
bad = int(suite.get("failures", 0)) + int(suite.get("errors", 0))
lines += ["", f"**{total - bad} of {total} tests passed.**"]

out = os.environ.get("GITHUB_STEP_SUMMARY")
text = "\n".join(lines) + "\n"
if out:
    with open(out, "a", encoding="utf-8") as f:
        f.write(text)
else:
    print(text)
