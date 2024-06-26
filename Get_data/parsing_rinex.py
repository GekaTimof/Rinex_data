import os
from gnss_tec import rnx
import json


# read all files in rinex directory convert each rnx file to json and save in directory
# at the end delete rinex directory
def pars_rinex(directory: str, raw_directory: str):
    # create directory for date
    if not os.path.exists(directory):
        os.mkdir(directory)

    # unpack rinex file and transform in to json files
    print("Start extracting rinex data to json")
    for file_rinex in os.listdir(raw_directory):
        file_link = directory + "/" + file_rinex[:-4] + ".json"
        file_rinex_link = raw_directory + "/" + file_rinex

        if file_rinex[-4:] == ".rnx":
            print(file_rinex)
            with open(file_rinex_link) as obs_file:
                data = {}
                try:
                    reader = rnx(obs_file)
                except Exception as err:
                    data["err"] = str(err)
                else:
                    for tec in reader:
                        if tec.timestamp:
                            if tec.timestamp not in data:
                                data[str(tec.timestamp)] = []
                            data[str(tec.timestamp)].append([tec.satellite, tec.phase_tec, tec.p_range_tec])


            # convert data to json and save it
            with open(file_link, 'w') as f:
                json.dump(data, f)

            # delete rinex
            os.remove(raw_directory + "/" + file_rinex)
    os.rmdir(raw_directory)
    print("Finish extracting rinex data to json")


