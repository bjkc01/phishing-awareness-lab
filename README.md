# phishing-awareness-lab

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Project overview

`phishing-awareness-lab` is a portfolio-ready cybersecurity lab that simulates phishing campaign design, employee response tracking, risk analysis, and targeted remediation training. It is built as an ethical training exercise for cybersecurity students or junior analysts to demonstrate defensive awareness, campaign management, and security reporting.

## Features

- Simulated phishing campaign assignment using CSV user data
- Employee interaction tracking for clicks, credential submissions, and reporting
- Calculated metrics for click rate, credential submission rate, reporting rate, and repeat offenders
- Automated markdown security report generation
- Realistic training content for awareness and remediation
- MITRE ATT&CK mapping for T1566 – Phishing

## Repository structure

- `docs/` – program documentation, phishing threat model, and awareness strategy
- `templates/` – safe phishing simulation email templates for awareness testing
- `training/` – employee awareness guide and remediation training resources
- `data/` – fake sample user data and campaign result data
- `scripts/` – Python scripts for campaign simulation, result analysis, and report generation
- `reports/` – sample campaign report and risk summary
- `assets/` – placeholder for diagrams, process maps, or screenshots

## Tools used

- Python 3.10+ standard library
- `csv` for structured data processing
- `pathlib` for file paths
- `datetime` for timestamped reporting
- Markdown for documentation and portfolio deliverables

## How to run scripts

1. Open a terminal in the repository root.
2. Run campaign simulation:
   ```bash
   python scripts/send_simulated_campaign.py
   ```
3. Analyze campaign results:
   ```bash
   python scripts/analyze_results.py
   ```
4. Generate a markdown security report:
   ```bash
   python scripts/generate_report.py
   ```

## Example workflow

1. Review `data/sample_users.csv` and `templates/`.
2. Execute `send_simulated_campaign.py` to simulate mail traffic and template assignment.
3. Use `analyze_results.py` to calculate metrics and identify high-risk users.
4. Generate a defensive report with `generate_report.py`.
5. Use `training/` content to recommend remediation pathways.

## MITRE ATT&CK reference

- **T1566 – Phishing**
- Simulated email campaign uses social engineering techniques to test user awareness.
- Focuses on human attack surface, credential theft, and detection/reporting behavior.

## Security & ethics disclaimer

This repository is purely defensive and educational. It does not send real email messages, it does not harvest valid credentials, and it does not include malicious tooling. All sample data is fictional and safe for public sharing.

## Resume-ready bullet points

- Designed a phishing awareness lab that models campaign simulation, risk scoring, and employee remediation.
- Built data-driven analysis scripts to measure click rates, credential submission rates, and reporting behavior.
- Documented MITRE ATT&CK mapping and security awareness strategy for T1566 – Phishing.
- Created training resources for targeted follow-up and user behavior improvement.

## Future improvements

- Add interactive dashboards or visualization outputs.
- Extend campaign simulation to support multiple campaign waves.
- Add role-based training assignments based on risk tier.
- Integrate anomaly detection for rapid repeat offender identification.
