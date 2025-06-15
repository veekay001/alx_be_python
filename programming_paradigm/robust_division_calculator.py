def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Both inputs must be numeric."
