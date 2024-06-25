from get_zip_rinex import get_zip_rinex
from unpack_data import unpack_data
from parsing_rinex import pars_rinex

# test datas
date = "2024-01-01"
directory = f"../Parsed_rinex_data/{date}"
link = f"https://api.simurg.space/datafiles/map_files?date={date}"
file_name = f"{date}.zip"


# get rinex zip file from link
get_zip_rinex(link=link, file_name=file_name)

# create directory and save unpacked data in it
get_data_zip(directory=directory, file_name=file_name)

