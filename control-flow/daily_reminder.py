task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

reminder = f"Task: '{task}' is marked as '{priority}' priority."

match priority:
    case "high":
        reminder += " Please focus on this task first."
    case "medium":
        reminder += " Attend to this after your high-priority tasks."
    case "low":
        reminder += " You can schedule this for later."
    case _:
        reminder += " (Unknown priority provided.)"

if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"
print("\n" + reminder)