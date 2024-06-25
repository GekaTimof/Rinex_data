import sys
import requests
from get_data_from_zip import get_data_zip

# test datas
date = "2024-01-01"
directory = f"../Parsed_rinex_data/{date}"
link = f"https://api.simurg.space/datafiles/map_files?date={date}"
file_name = f"{date}.zip"

# get rinex zip file from link
with open(file_name, "wb") as f:
    print("Start downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()
    print("Finish downloading %s" % file_name)

# create directory and save unpacked data in it
get_data_zip(directory, file_name)



