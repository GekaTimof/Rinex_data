import os
from gnss_tec import rnx
import json

# test datas
date = "2024-01-01"
directory = f"../Parsed_rinex_data/{date}"


# read all files in rinex directory convert each rnx file to json and save in directory
# at the end delete rinex directory
def pars_rinex(directory: str):
    # get rinex directory
    directory_rinex = directory + "-rinex"

    # create directory for date
    if not os.path.exists(directory):
        os.mkdir(directory)

    # unpack rinex file and transform in to json files
    print("Start extracting rinex data to json")
    for file_rinex in os.listdir(directory_rinex):
        file_link = directory + "/" + file_rinex[:-4] + ".json"
        file_rinex_link = directory_rinex + "/" + file_rinex
        print(file_rinex_link)
        with open(file_rinex_link) as obs_file:
            data = {}
            try:
                reader = rnx(obs_file)
                for tec in reader:
                    if tec.timestamp:
                        if tec.timestamp not in data:
                            data[str(tec.timestamp)] = []
                        data[str(tec.timestamp)].append([tec.satellite, tec.phase_tec, tec.p_range_tec])
            except Exception as err:
                data["err"] = str(type(err))

        # convert data to json and save it
        with open(file_link, 'w') as f:
            json.dump(data, f)

        # delete rinex
        os.remove(directory_rinex + "/" + file_rinex)
    os.rmdir(directory_rinex)
    print("Finish extracting rinex data to json")


