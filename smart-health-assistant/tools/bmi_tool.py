

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Convert height and calculate BMI."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)
