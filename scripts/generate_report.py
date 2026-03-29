#!/usr/bin/env python3
"""Generate a markdown security report from phishing campaign results."""

import csv
from datetime import date
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RESULTS_CSV = ROOT_DIR / "data" / "phishing_results_sample.csv"
REPO_REPORT = ROOT_DIR / "reports" / "sample_campaign_report.md"


def normalize_flag(value):
    return str(value).strip().lower() == "yes"


def load_results(path):
    with path.open(newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


def calculate_metrics(rows):
    total = len(rows)
    clicked = sum(normalize_flag(row["clicked"]) for row in rows)
    submitted = sum(normalize_flag(row["submitted"]) for row in rows)
    reported = sum(normalize_flag(row["reported"]) for row in rows)
    return {
        "total_responses": total,
        "click_rate": clicked / total if total else 0,
        "credential_submission_rate": submitted / total if total else 0,
        "reporting_rate": reported / total if total else 0,
    }


def determine_risk(metrics):
    if metrics["credential_submission_rate"] >= 0.15:
        return "High"
    if metrics["click_rate"] >= 0.30:
        return "Medium"
    return "Low"


def build_report(metrics):
    risk_level = determine_risk(metrics)
    return f"""# Sample Campaign Report

Generated: {date.today().isoformat()}

## Executive summary

This report summarizes the simulated phishing campaign and identifies key awareness gaps.

## Campaign metrics

- Total campaign responses: {metrics['total_responses']}
- Click rate: {metrics['click_rate'] * 100:.1f}%
- Credential submission rate: {metrics['credential_submission_rate'] * 100:.1f}%
- Reporting rate: {metrics['reporting_rate'] * 100:.1f}%
- Risk level: **{risk_level}**

## Risk analysis

The simulated campaign results show measurable phishing susceptibility in the employee population. A higher click rate indicates that users are engaging with suspicious content, while credential submissions highlight the critical need for additional verification training.

## Recommendations

1. Assign targeted remediation training to repeat offenders and employees with overdue awareness status.
2. Reinforce reporting behavior by promoting the phishing report channel and response process.
3. Conduct a follow-up campaign within 30 days to measure improvement.
4. Update the security awareness program to include sample email reviews and scenario-based exercises.

## Next steps

- Use `training/remediation-training-targeted.md` for high-risk remediation.
- Use `training/remediation-training-basic.md` for low- and medium-risk refreshers.
- Align future campaigns with the MITRE ATT&CK T1566 phishing model.

## Disclaimer

This report is based on fictional sample data in `data/phishing_results_sample.csv` and is intended for educational awareness and defensive training.
"""


def write_report(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    if not RESULTS_CSV.exists():
        print(f"Missing results file: {RESULTS_CSV}")
        return

    rows = load_results(RESULTS_CSV)
    metrics = calculate_metrics(rows)
    report = build_report(metrics)
    write_report(REPO_REPORT, report)
    print(f"Generated report: {REPO_REPORT}")


if __name__ == "__main__":
    main()
