# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature (e.g., 32F or 0C): ").strip().upper()

        if temp_input.endswith("F"):
            temp_value = float(temp_input[:-1])
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C")

        elif temp_input.endswith("C"):
            temp_value = float(temp_input[:-1])
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F")

        else:
            raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Invalid temperature. Please enter a numeric value. ({ve})")

if __name__ == "__main__":
    main()