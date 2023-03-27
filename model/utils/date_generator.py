import datetime
from datetime import date
import random


def date_generate():
    start = date(1900, 10, 1)
    end = datetime.date(2022, 11, 30)

    num_days = (end - start).days
    random_days = random.randint(1, num_days)
    random_date = start + datetime.timedelta(days=random_days)
    return random_date.strftime("%d %m %Y")
