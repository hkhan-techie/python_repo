from datetime import date, datetime, timedelta

print(f'end_date :',(date.today()).strftime("%Y-%m-%d"))
print(f'start_date :',(datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d"))

