#!/usr/bin/env python3
"""Analyze phishing campaign results and calculate key metrics."""

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RESULTS_CSV = ROOT_DIR / "data" / "phishing_results_sample.csv"
USERS_CSV = ROOT_DIR / "data" / "sample_users.csv"


def normalize_flag(value):
    return str(value).strip().lower() == "yes"


def load_results(path):
    results = []
    with path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)
    return results


def load_users(path):
    users = {}
    with path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users[row["user_id"]] = row
    return users


def calculate_metrics(rows):
    total = len(rows)
    clicked = sum(normalize_flag(row["clicked"]) for row in rows)
    submitted = sum(normalize_flag(row["submitted"]) for row in rows)
    reported = sum(normalize_flag(row["reported"]) for row in rows)

    per_user = defaultdict(int)
    offender_counts = Counter()

    for row in rows:
        user_id = row["user_id"]
        action = normalize_flag(row["clicked"]) or normalize_flag(row["submitted"])
        if action:
            per_user[user_id] += 1
        offender_counts[user_id] += 1

    repeat_offenders = sum(1 for user, count in offender_counts.items() if count > 1)

    return {
        "total_responses": total,
        "click_rate": clicked / total if total else 0,
        "credential_submission_rate": submitted / total if total else 0,
        "reporting_rate": reported / total if total else 0,
        "repeat_offenders": repeat_offenders,
        "actions_by_user": per_user,
    }


def format_percentage(value):
    return f"{value * 100:.1f}%"


def print_summary(metrics):
    print("Phishing campaign analysis summary")
    print("---")
    print(f"Total campaign responses: {metrics['total_responses']}")
    print(f"Click rate: {format_percentage(metrics['click_rate'])}")
    print(f"Credential submission rate: {format_percentage(metrics['credential_submission_rate'])}")
    print(f"Reporting rate: {format_percentage(metrics['reporting_rate'])}")
    print(f"Repeat offenders: {metrics['repeat_offenders']}")
    print("---")
    if metrics["actions_by_user"]:
        print("Users with multiple campaign interactions:")
        for user_id, count in sorted(metrics["actions_by_user"].items()):
            if count > 1:
                print(f"  - {user_id}: {count} triggered actions")


def main():
    if not RESULTS_CSV.exists():
        print(f"Missing results file: {RESULTS_CSV}")
        return

    rows = load_results(RESULTS_CSV)
    metrics = calculate_metrics(rows)
    print_summary(metrics)


if __name__ == "__main__":
    main()
