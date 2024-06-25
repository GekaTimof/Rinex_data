import os
import zipfile

# test datas
#date = "2024-01-01"
#directory = f"../Parsed_rinex_data/{date}"
#file_name = f"{date}.zip"


# create directory and save unpacked data in it
def get_data_zip(directory, file_name):
    # create directory for date
    if not os.path.exists(directory):
        os.mkdir(directory)

    # extracting data from zip
    with zipfile.ZipFile(file_name, 'r') as zip_file:
        print("Start extracting %s" % file_name)
        zip_file.extractall(directory)
        print("Finish extracting %s" % file_name)

    #delete zip file
    os.remove(file_name)

#get_data_zip(directory, file_name)
