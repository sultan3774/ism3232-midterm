SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7
STANDARD_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20
NO_DISCOUNT = 0.0


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before any discount."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate for the rental."""
    if days >= LONG_RENTAL_DAYS:
        return LONG_RENTAL_DISCOUNT
    if days >= SHORT_RENTAL_DAYS or contractor:
        return STANDARD_DISCOUNT
    return NO_DISCOUNT
