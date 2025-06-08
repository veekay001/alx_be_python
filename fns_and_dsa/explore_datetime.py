
from datetime import datetime, timedelta


display_current_datetime =datetime.now()

current_date = display_current_datetime.strftime("%Y-%m-%d,%H:%M:%S")

print("Current date and time:",current_date)

calculate_future_date = int(input("Enter the number of days to add to the current date:"))

future_date = current_date + timedelta(days=10)

format_fd = future_date.strftime("%Y-%m-%d")

print("Future date:", format_fd)