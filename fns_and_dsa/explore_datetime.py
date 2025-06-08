
from datetime import datetime, timedelta


current_date = datetime.now()

format = current_date.strftime("%Y-%m-%d,%H:%M:%S")

print("Current date and time:",format)

calculate_future_date = int(input("Enter the number of days to add to the current date:"))

future_date = current_date + timedelta(days=10)

format_fd = future_date.strftime("%Y-%m-%d")

print("Future date:", format_fd)