from gnss_tec import rnx
import json

file_name = 'DAEJ00KOR_R_20240010000_01D_30S_MO.rnx'

def parsRinex(file_name: str):
    with open(file_name) as obs_file:
        reader = rnx(obs_file)
        data = {}

        for tec in reader:
            if tec.timestamp not in data:
                data[tec.timestamp] = []

            data[tec.timestamp].append([tec.satellite, tec.phase_tec, tec.p_range_tec])


    # convert data to json
    data_json = json.dumps(data)
    return data_json

parsRinex(file_name)

