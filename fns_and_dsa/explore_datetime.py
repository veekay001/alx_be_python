
from datetime import datetime, timedelta

def display_current_datetime():
    
  current_date = datetime.now()

  formated_date = current_date.strftime("%Y-%m-%d,%H:%M:%S")

  print("Current date and time:",formated_date)

calculate_future_date = int(input("Enter the number of days to add to the current date:"))

future_date = current_date + timedelta(days=10)

format_fd = future_date.strftime("%Y-%m-%d,%H:%M:%S")

print("Future date:", format_fd)

if __name__ == "__main__":
    display_current_datetime()