
from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()

    current_date = current_date.strftime("%Y-%m-%d,%H:%M:%S")

    print("Current date and time:",formated_date)
  
number_of_days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    
 current_date = datetime.now()

 future_date = current_date + timedelta(days=10)

 formated_date = future_date.strftime("%Y-%m-%d")

 print("Future date:", formated_date)
