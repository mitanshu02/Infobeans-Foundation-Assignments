duration = int(input("Total seconds = "))

hours = duration//3600
rem_seconds_from_hour = duration%3600

minutes = rem_seconds_from_hour//60
seconds = rem_seconds_from_hour % 60

print(f"Hours = {hours}")
print(f"Minutes = {minutes}")
print(f"Seconds = {seconds}")