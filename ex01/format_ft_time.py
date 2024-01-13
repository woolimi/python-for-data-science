from datetime import datetime

current_date = datetime.now()
timestamp = datetime.timestamp(current_date)
print(f"Seconds since January 1, 1970: {'{:,.4f}'.format(timestamp)}\
 or {'{:.2e}'.format(timestamp)} in scientific notation")
print(current_date.strftime("%b %d %Y"))
