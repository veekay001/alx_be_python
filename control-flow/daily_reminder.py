task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

reminder = f"Task: '{task}' is marked as '{priority}' priority."

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' has an unknown priority level."

if time_bound == "yes" and priority in ["high", "medium"]:

    reminder = reminder + " that requires immediate attention today!"

print( "\n" + reminder)