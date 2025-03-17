from datetime import date,time
import datetime
import pytz
nz_timezone = pytz.timezone("Pacific/Auckland")
nz_time = datetime.datetime.now(nz_timezone)
print("New Zealand Time : " , nz_time.strftime("%H:%M:%S"))