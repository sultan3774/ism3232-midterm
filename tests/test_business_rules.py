from business_rules import calculate_rental_cost, get_rental_discount


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
