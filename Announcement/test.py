from datetime import date, datetime
currentDate = date.today()

currentTime = datetime.today().strftime("%I:%M %p")

print(currentTime)
