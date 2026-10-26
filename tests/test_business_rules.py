from business_rules import calculate_rental_cost, get_rental_discount
from business_rules import calculate_quote


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
