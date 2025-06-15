
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_str = input("Enter the temperature to convert: ").strip()
        temp_value = float(temp_str)  # Raises ValueError if not numeric

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as ve:
        print(f"Invalid temperature. Please enter a numeric value. ({ve})")

if __name__ == "__main__":
    main()