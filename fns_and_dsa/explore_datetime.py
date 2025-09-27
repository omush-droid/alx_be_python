"""
explore_datetime.py

Demonstrates use of Python's datetime module:
- Display current date and time
- Calculate a future date after adding a number of days
"""

from datetime import datetime, timedelta  # ✅ import datetime module

def display_current_datetime() -> str:
    """
    Get and return the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()   # ✅ save current date
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date   # ✅ return formatted date (check requires this)


def calculate_future_date(days: int) -> str:
    """
    Calculate and return the future date after adding 'days' to today.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # ✅ save future date
    return future_date.strftime("%Y-%m-%d")   # return formatted future date


def main():
    # Part 1: Display current date and time
    print("Current date and time:", display_current_datetime())

    # Part 2: Ask user for number of days
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("Future date:", calculate_future_date(num_days))


if __name__ == "__main__":
    main()
