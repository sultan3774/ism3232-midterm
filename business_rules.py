SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7
STANDARD_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20
NO_DISCOUNT = 0.0
DAMAGE_WAIVER_LIMIT = 150.0
DAMAGE_WAIVER_FEE = 25.0
DEPOSIT_LIMIT = 1000.0
INSPECTION_MIN_DAYS = 5
INSPECTION_QUOTE_LIMIT = 800.0


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


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the discounted rental cost plus any damage waiver."""
    rental_cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    quote = rental_cost * (1 - discount)

    if quote < DAMAGE_WAIVER_LIMIT:
        quote += DAMAGE_WAIVER_FEE

    return quote


def requires_deposit(quote: float) -> bool:
    """Return whether the quote requires a deposit."""
    return quote >= DEPOSIT_LIMIT


def needs_inspection(days: int, quote: float) -> bool:
    """Return whether the rental needs a pickup inspection."""
    return days >= INSPECTION_MIN_DAYS and quote > INSPECTION_QUOTE_LIMIT
