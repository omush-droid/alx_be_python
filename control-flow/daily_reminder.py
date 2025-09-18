
# daily_reminder.py
# A program that reminds the user of a single priority task for the day.

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify message if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["medium", "low"]:
        message += ". Consider completing it when you have free time."

# Output the Customized Reminder
print(message)
