#Userr prompts
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case based on priority
match priority:
    case "high":
        reminder = f"High priority - {task}"
    case "medium":
        reminder = f"Medium priority - {task}"
    case "low":
        reminder = f"Low priority - {task}"
    case _:
        reminder = f"Unknown priority - {task}"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " – This task requires immediate attention today!"

print("Reminder:", reminder)

     
        