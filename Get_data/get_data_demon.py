from create_data_directorys import create_data_directorys
from get_zip_rinex import get_zip_rinex
from unpack_data import unpack_data
from parsing_rinex import pars_rinex

# test datas
date = "2024-01-01"

# constant datas
all_raw_data_directory = "../Raw_data"
all_parsed_rinex_data_directory = "../Parsed_rinex_data"
all_demons_directory = "../Demons"

# calculating constant data
raw_directory = f"../Raw_data/{date}"
directory = f"../Parsed_rinex_data/{date}"
link = f"https://api.simurg.space/datafiles/map_files?date={date}"
file_name = f"{date}.zip"

# create directorys for all datas if they not exist
create_data_directorys([all_raw_data_directory, all_parsed_rinex_data_directory, all_demons_directory])

# get rinex zip file from link
get_zip_rinex(link=link, raw_directory=raw_directory, file_name=file_name)

# create directory and save unpacked data in it
unpack_data(raw_directory=raw_directory, file_name=file_name)

# read all files in rinex directory convert each rnx file to json and save in directory
# at the end delete rinex directory
pars_rinex(directory=directory, raw_directory=raw_directory)
