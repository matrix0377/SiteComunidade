from datetime import datetime, timedelta, timezone

# UTC + 5:00 (Pakistan, India, Bangladesh, Nepal, Sri Lanka, and Bhutan time zone)
dt1 = datetime.now(tz=timezone(timedelta(hours=5)))
print(dt1)

# UTC + 7:00 (Vietnam, Thailand, and Indonesia time zone)
dt2 = datetime.now(tz=timezone(timedelta(hours=7)))
print(dt2)

# UTC - 3:00 (Argentina, Brazil, Chile, Paraguay, Uruguay, and Falkland Islands time zone)
dt3 = datetime.now(tz=timezone(timedelta(hours=-3)))
print(dt3)

