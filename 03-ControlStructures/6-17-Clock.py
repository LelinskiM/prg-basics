Time_24 = input("Enter time in 24-hour format (HH:MM): ")
Hours, Minutes = map(int, Time_24.split(":"))

if Hours > 12:
    Hours -= 12
    print(f"Time in 12-hour format: {Hours}:{Minutes} PM")
else:
    print(f"Time in 12-hour format: {Hours}:{Minutes} AM")