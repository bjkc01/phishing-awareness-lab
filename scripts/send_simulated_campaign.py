#!/usr/bin/env python3
"""Simulate a phishing campaign using sample user data."""

import csv
import random
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
USERS_CSV = ROOT_DIR / "data" / "sample_users.csv"
TEMPLATES = [
    "credential_harvest_email.txt",
    "invoice_phishing_email.txt",
    "password_reset_email.txt",
]

TEMPLATE_MAP = {
    "credential_harvest_email.txt": "Credential verification simulation",
    "invoice_phishing_email.txt": "Fake invoice review simulation",
    "password_reset_email.txt": "Password reset awareness simulation",
}


def load_users(path):
    users = []
    with path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users


def choose_template(user):
    status = user.get("training_status", "").lower()
    department = user.get("department", "").lower()

    if status in {"overdue", "not started"}:
        return TEMPLATES[0]
    if department == "finance":
        return TEMPLATES[1]
    if department == "engineering":
        return TEMPLATES[2]
    return random.choice(TEMPLATES)


def simulate_campaign(users):
    assignments = []
    print("Simulated phishing campaign assignment")
    print("(No real email is sent. This is a defensive training simulation.)")
    print("---")

    for user in users:
        template_file = choose_template(user)
        assignments.append((user["user_id"], user["name"], user["email"], template_file))
        print(
            f"User: {user['name']} <{user['email']}> assigned template: {template_file}"
        )

    print("---")
    print(f"Total users simulated: {len(assignments)}")
    return assignments


def main():
    if not USERS_CSV.exists():
        print(f"Missing user data file: {USERS_CSV}")
        return

    users = load_users(USERS_CSV)
    simulate_campaign(users)


if __name__ == "__main__":
    main()
