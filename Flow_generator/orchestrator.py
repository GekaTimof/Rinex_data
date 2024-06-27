import os
import datetime

# how much day ago we get data
delay = 4

# test datas
date = "2024-01-01"
start_date = datetime.date.today() - datetime.timedelta(days=delay) + datetime.timedelta(days=1)

# const data
all_demons_directory = "../Demons"
demons_directory = "/etc/systemd/system"

# calculating constant data
directory = f"../Parsed_rinex_data/{date}"


if not os.path.exists(directory):
    exit()

# create demon for each json
for file_name in os.listdir(directory):
    # create directory for demons
    #if not os.path.exists(all_demons_directory + "/" + start_date.strftime('%Y-%m-%d')):
    #    os.mkdir(all_demons_directory + "/" + start_date.strftime('%Y-%m-%d'))

    if file_name[-5:] == ".json":
        demon = f"""[Unit]
Description=Demon to send data to data flow
After=multi-user.target

[Service]
User=root
Group=root
Type=simple
Restart=always
ExecStart=/usr/bin/python3 send_data.py {start_date} {directory + "/" + file_name} {file_name[:4]}
        
[Install]
WantedBy=multy-user.target"""

        # create demon file
        f = open(demons_directory + "/" + start_date.strftime('%Y-%m-%d') + "&&" + file_name[:-5] + ".service", "w")
        f.write(demon)
        f.close()









