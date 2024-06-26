import os
import zipfile
import gzip
import shutil

# shell command CRX2RNX
crx2rnx = "CRX2RNX"


# create raw_directory and save unpacked data in it
def unpack_data(raw_directory, file_name):
    # create raw_directory for date
    if not os.path.exists(raw_directory):
        os.mkdir(raw_directory)

    # extracting data from zip
    with zipfile.ZipFile(raw_directory + "/" + file_name, 'r') as zip_file:
        print("Start extracting %s" % file_name)
        zip_file.extractall(raw_directory)
        print("Finish extracting %s" % file_name)
    # delete zip file
    os.remove(raw_directory + "/" + file_name)

    # unpack gz files
    print("Start extracting rinex data from gz")
    for file_gz in os.listdir(raw_directory):
        file_link = raw_directory + "/" + file_gz

        if file_gz[-3:] == ".gz":
            with gzip.open(file_link, 'rb') as f_in:
                with open(file_link[:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

        if file_gz[-4:] != ".cnx":
            os.remove(file_link)
    print("Finish extracting rinex data from gz")

    # convert crx to rnx
    print("Start converting crx to rnx")
    for file_crx in os.listdir(raw_directory):
        file_link = raw_directory + "/" + file_crx

        if file_link[-4:] == ".crx":
            # build shell command
            shell_command = ''.join([crx2rnx, " ", file_link])
            # run shell command
            os.system(shell_command)

        if file_crx[-4:] != ".rnx":
            os.remove(file_link)
    print("Finish converting crx to rnx")
