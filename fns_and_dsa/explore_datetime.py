from datetime import datetime 

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted)

display_current_datetime()


def calculate_future_date():
    current_date = datetime.datetime.now()
    user_input = int(input("Enter the number of days to the current date: "))
    future_delta = datetime.timedelta(days=user_input)
    future_date = current_date + future_delta
    
    print("Future date:", future_date.strftime("%Y-%m-%d"))

calculate_future_date()