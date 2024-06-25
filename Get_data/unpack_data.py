import os
import zipfile
import gzip
import shutil

# test datas
date = "2024-01-01"
directory = f"../Parsed_rinex_data/{date}"
#file_name = f"{date}.zip"

# shell command CRX2RNX
crx2rnx = "CRX2RNX"

# create directory and save unpacked data in it
def unpack_data(directory, file_name):
    # get rinex directory
    directory += "-rinex"

    # create directory for date
    if not os.path.exists(directory):
        os.mkdir(directory)

    # extracting data from zip
    with zipfile.ZipFile(file_name, 'r') as zip_file:
        print("Start extracting %s" % file_name)
        zip_file.extractall(directory)
        print("Finish extracting %s" % file_name)
    # delete zip file
    os.remove(file_name)

    # unpack gz files
    print("Start extracting rinex data from gz")
    for file_gz in os.listdir(directory):
        file_link = directory + "/" + file_gz

        if file_gz[-3:] == ".gz":
            with gzip.open(file_link, 'rb') as f_in:
                with open(file_link[:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

    # delete not cnx data
    for file_gz in os.listdir(directory):
        file_link = directory + "/" + file_gz
        if file_gz[-4:] != ".cnx":
            os.remove(file_link)
    print("Finish extracting rinex data from gz")

    # convert crx to rnx
    directory += "-rinex"
    print("Start converting crx to rnx")
    for file_crx in os.listdir(directory):
        file_link = directory + "/" + file_crx

        if file_link[-4:] == ".crx":
            # build shell command
            shell_command = ''.join([crx2rnx, " ", file_link])
            # run shell command
            os.system(shell_command)

            os.remove(file_link)
    print("Finish converting crx to rnx")
