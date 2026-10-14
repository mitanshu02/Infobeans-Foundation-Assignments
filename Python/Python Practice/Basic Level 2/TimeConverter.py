duration = int(input(" Enter the Total event duration in seconds: "))

hours = duration//3600
rem_seconds_from_hour = duration%3600

minutes = rem_seconds_from_hour//60
seconds = rem_seconds_from_hour % 60

print("Hours: {}, Minutes: {}, Seconds: {}".format(hours,minutes,seconds))