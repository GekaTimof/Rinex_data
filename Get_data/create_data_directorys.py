import os

# create directorys for all datas if they not exist
def create_data_directorys(directorys: list[str]):
    # create all directorys
    for directory in directorys:
        if not os.path.exists(directory):
            os.mkdir(directory)
