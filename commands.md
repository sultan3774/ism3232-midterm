# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
These commands were recovered from my terminal screenshots. The original terminal history was unavailable, so this record is incomplete.

```bash
python -m pip install pytest ruff
python -m pip freeze > requirements.txt
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
code .
source .venv/bin/activate
deactivate
printf '.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
```

## 2. The virtual environment
```bash
which python3
```

```text
/home/Sultan/ism3232-midterm/.venv/bin/python3
```

The path includes .venv/bin/python3, which shows that the virtual environment is active.

## 3. The project structure
```bash
tree -L 2
```
```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
The __pycache__ folder exists on my computer but is excluded from GitHub because it is listed in .gitignore.
## 4. Every function and test
```bash
rg 'def '
```

```text
tests/test_business_rules.py
8:def test_rental_cost():
12:def test_two_days_no_discount():
16:def test_three_days_discount():
20:def test_six_days_discount():
24:def test_seven_days_discount():
28:def test_contractor_changes_discount():
33:def test_contractor_keeps_long_rental_discount():
37:def test_quote_adds_damage_waiver():
41:def test_quote_for_contractor():
45:def test_quote_below_waiver_limit():
49:def test_quote_at_waiver_limit():
53:def test_quote_uses_discounted_cost_for_waiver():
57:def test_quote_with_long_rental_discount():
61:def test_deposit_below_limit():
65:def test_deposit_at_limit():
69:def test_inspection_below_days_limit():
73:def test_inspection_at_days_limit():
77:def test_inspection_at_quote_limit():
81:def test_inspection_above_quote_limit():
85:def test_total_quoted_short_list():
93:def test_total_quoted_empty_list():
97:def test_largest_rental_short_list():
105:def test_largest_rental_tie_returns_first():
113:def test_largest_rental_empty_list():
117:def test_format_rental_line_no_flags():
123:def test_format_rental_line_yes_flags():

business_rules.py
13:def calculate_rental_cost(daily_rate: float, days: int) -> float:
18:def get_rental_discount(days: int, contractor: bool = False) -> float:
27:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
39:def requires_deposit(quote: float) -> bool:
44:def needs_inspection(days: int, quote: float) -> bool:
49:def total_quoted(rentals: list) -> float:
59:def largest_rental(rentals: list) -> str:
77:def format_rental_line(
```
business_rules.py defines 8 functions, and tests/test_business_rules.py defines 26 tests.

## 5. Which files print
```bash
rg -l 'print'
```

```text
commands.md
main.py
```

main.py prints the report. business_rules.py returns values and does not contain print calls.

## 6. The commit history