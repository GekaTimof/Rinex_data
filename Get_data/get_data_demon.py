from get_zip_rinex import get_zip_rinex
from unpack_data import unpack_data
from parsing_rinex import pars_rinex

# test datas
date = "2024-01-01"
raw_directory = f"../Raw_data/{date}"
directory = f"../Parsed_rinex_data/{date}"
link = f"https://api.simurg.space/datafiles/map_files?date={date}"
file_name = f"{date}.zip"


# get rinex zip file from link
#get_zip_rinex(link=link, raw_directory=raw_directory, file_name=file_name)

# create directory and save unpacked data in it
unpack_data(raw_directory=raw_directory, file_name=file_name)

# read all files in rinex directory convert each rnx file to json and save in directory
# at the end delete rinex directory
pars_rinex(directory=directory, raw_directory=raw_directory)
