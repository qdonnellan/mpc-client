from decimal import Decimal, InvalidOperation


def convert_to_decimal(number):
    """Convert the number to a decimal, if possible. If not possible return
    None
    """
    try:
        return Decimal(number)
    except InvalidOperation:
        return None
