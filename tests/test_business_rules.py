from business_rules import calculate_rental_cost, get_rental_discount
from business_rules import calculate_quote
from business_rules import requires_deposit, needs_inspection


def test_rental_cost():
    assert round(calculate_rental_cost(60.0, 2), 2) == 120.0


def test_two_days_no_discount():
    assert get_rental_discount(2) == 0.0


def test_three_days_discount():
    assert get_rental_discount(3) == 0.10


def test_six_days_discount():
    assert get_rental_discount(6) == 0.10


def test_seven_days_discount():
    assert get_rental_discount(7) == 0.20


def test_contractor_changes_discount():
    assert get_rental_discount(2, False) == 0.0
    assert get_rental_discount(2, True) == 0.10


def test_contractor_keeps_long_rental_discount():
    assert get_rental_discount(7, True) == 0.20


def test_quote_adds_damage_waiver():
    assert round(calculate_quote(60.0, 2), 2) == 145.0


def test_quote_for_contractor():
    assert round(calculate_quote(60.0, 2, True), 2) == 133.0


def test_quote_below_waiver_limit():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_quote_at_waiver_limit():
    assert round(calculate_quote(150.0, 1), 2) == 150.0


def test_quote_uses_discounted_cost_for_waiver():
    assert round(calculate_quote(160.0, 1, True), 2) == 169.0


def test_quote_with_long_rental_discount():
    assert round(calculate_quote(120.0, 10), 2) == 960.0


def test_deposit_below_limit():
    assert requires_deposit(999.99) is False


def test_deposit_at_limit():
    assert requires_deposit(1000.0) is True


def test_inspection_below_days_limit():
    assert needs_inspection(4, 900.0) is False


def test_inspection_at_days_limit():
    assert needs_inspection(5, 900.0) is True


def test_inspection_at_quote_limit():
    assert needs_inspection(5, 800.0) is False


def test_inspection_above_quote_limit():
    assert needs_inspection(5, 800.01) is True
