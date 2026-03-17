# SDET Framework

![Playwright Tests](https://github.com/AmrozM/SDET_Folder_Structure/actions/workflows/playwright_tests.yml/badge.svg)

## Project Overview
This project automates UI and API testing. UI tests cover Bromcom MIS login with navigation to Student profile and MAT Vision login across multiple environments (Team5, Release, Hotfix). With the help of ENV variables tests can run on both products i.e MIS and Vision just by using a single env variable e.g: Team5. API tests cover JSONPlaceholder API validation. Custom Playwright fixtures are used instead of pytest-playwright plugin. Logger is implemented for test execution visibility. CI is implemented so that every time code is pushed to GitHub the pipeline runs and all test cases are executed. GitHub secrets are used to securely store credentials.

## Tech Stack
- Python
- Playwright (sync_api)
- Pytest
- Requests (API testing)

## Framework Structure
```
sdet_framework/
├── config/         → Environment config (URLs, credentials)
├── pages/          → Page Object Model classes
├── tests/          → Test files
├── test_data/      → JSON files having test data
├── utils/          → Logger and helpers
├── conftest.py     → Custom Playwright fixtures
├── pytest.ini      → Pytest configuration
└── requirements.txt
```

## How to Run Tests

Run MIS test:
```bash
$env:ENV="Team5"
pytest tests/test_Login_MIS_Team5.py -v
```

Run Vision test:
```bash
$env:ENV="Team5"
pytest tests/test_Login_vision.py -v
```

Run with logs:
```bash
pytest tests/test_Login_MIS_Team5.py -v -s
```

Run all tests:
```bash
$env:ENV="Team5"
pytest -v
```

Run and generate HTML report:
```bash
pytest -v --html=report.html
```

## Environment Variables

Set environment (PowerShell):
```powershell
$env:ENV="Team5"   # MIS + Vision Team5 server
$env:ENV="Release" # MIS + Vision Release server
$env:ENV="Hotfix"  # MIS + Vision Hotfix server
```

Run headed (browser visible):
```powershell
$env:HEADED="true"
pytest tests/test_Login_MIS_Team5.py -v
```