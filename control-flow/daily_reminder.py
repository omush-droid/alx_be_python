# daily_reminder.py
# A program that provides a customized reminder for a single task
# using conditional statements, match case, and loops.

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 1: Base reminder depending on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Step 2: Customize reminder depending on time sensitivity
if time_bound == "yes":
    reminder = f"Reminder: {reminder} that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Step 3: Output the Customized Reminder
print(reminder)

