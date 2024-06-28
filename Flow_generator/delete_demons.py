import os
import datetime
from dateutil.parser import parse

# const data
demons_directory = '/etc/systemd/system'

# how much day ago we get data
delay = 4

# test datas
date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d")
#date = datetime.date.today() - datetime.timedelta(days=delay)


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

# delete all old demons in demons_directory
for file_name in os.listdir(demons_directory):
    if is_date(file_name[:10]) and datetime.datetime.strptime(file_name[:10], "%Y-%m-%d") < date:
        os.remove(demons_directory + "/" + file_name)