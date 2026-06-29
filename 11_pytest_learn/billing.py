def calculate_total(price: float, discount: float = 0) -> float:
    """Calculates the final price after a flat discount wrapper."""
    if price < 0 or discount < 0:
        raise ValueError("Inputs cannot be negative")
    return price * (1 - (discount/100))