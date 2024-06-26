import sys
#import requests
import os
import wget

# get rinex zip file from link
def get_zip_rinex(link: str, raw_directory: str, file_name: str):
    with open(file_name, "wb") as f:
        # create directory for raw date
        if not os.path.exists(raw_directory):
            os.mkdir(raw_directory)

        # get raw data from link and save it in directory
        print("Start downloading %s" % file_name)
        wget.download(link, out=raw_directory)
        print("Finish downloading %s" % file_name)


