# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Sultan Alsereidi
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program calculates tool rental quotes for eight customers. It applies discounts and damage waiver fees and checks whether a deposit or inspection is required. It prints each rental and a summary of the results.

## Business Rules

1. The rental cost is the daily rate multiplied by the number of days.
2. Rentals of 3–6 days receive a 10% discount. Rentals of 7 or more days receive a 20% discount.
3. Contractors receive at least a 10% discount. Discounts do not stack.
4. A $25 damage waiver fee is added when the discounted rental cost is below $150.
5. A deposit is required when the final quote is $1,000 or more.
6. An inspection is required when the rental lasts at least 5 days and the final quote is more than $800.

## How to Run

Run these commands from the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## How to Test

The project contains 26 tests.

```bash
ruff format .
ruff check .
pytest -v
```

## Files in This Repository

- `business_rules.py`: Contains the eight business rule functions and named constants.
- `main.py`: Contains the rental data and prints the report and summary.
- `tests/__init__.py`: Marks the tests folder as a Python package.
- `tests/test_business_rules.py`: Contains the 26 tests.
- `requirements.txt`: Lists the Python dependencies and their versions.
- `.gitignore`: Excludes the virtual environment and cache folders from Git.
- `commands.md`: Records terminal commands, outputs, and explanations.
- `README.md`: Explains the program and how to run and test it.

## AI Use Statement

I did not use AI