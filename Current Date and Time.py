from datetime import date, time, datetime

today = date.today()
print(today)

now = datetime.now()
print(now)

print(f"Current year: {today.year}")
print(f"Current month: {today.month}")
(print(f"Current Day: {today.day}"))