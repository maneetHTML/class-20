import datetime
import random
start_date = datetime.date(2024,1,1)
end_date = datetime.date(2025,1,1)
num_days = (end_date - start_date).days
rand_days = random.randint(1,num_days)
random_date = start_date +datetime.timedelta(days=rand_days)
print(random_date)