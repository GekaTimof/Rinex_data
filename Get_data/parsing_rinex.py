import os
from gnss_tec import rnx
import json

# test datas
date = "2024-01-01"
directory = f"../Parsed_rinex_data/{date}"


def pars_rinex(directory: str):
    directory_rinex = directory + "-rinex"

    # create directory for date
    if not os.path.exists(directory):
        os.mkdir(directory)

    # unpack rinex file and transform in to json files
    print("Start extracting rinex data to json")
    for file_rinex in os.listdir(directory_rinex):
        file_link = directory_rinex + "/" + file_rinex
        print(file_link)
        with open(file_link) as obs_file:
            reader = rnx(obs_file)
            data = {}

            for tec in reader:
                if tec.timestamp not in data:
                    data[tec.timestamp] = []

                data[tec.timestamp].append([tec.satellite, tec.phase_tec, tec.p_range_tec])

        # convert data to json and save it
        with open(file_link[:-4]) as f:
            json.dump(data, f)

        # delete rinex
        #os.remove(directory_rinex + "/" + file_rinex)

    print("Finish extracting rinex data to json")


pars_rinex(directory=directory)
