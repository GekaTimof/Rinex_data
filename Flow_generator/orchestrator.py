import os
import datetime
import time

# how much day ago we get data
delay = 4

# test datas
date = "2024-01-01"
#date = datetime.date.today() - datetime.timedelta(days=delay)
#start_date = datetime.date.today() - datetime.timedelta(days=delay) + datetime.timedelta(days=1)
start_date = datetime.datetime.strptime("2024-01-01", "%Y-%m-%d").date()

# const data
demons_directory = '/etc/systemd/system'

# calculating constant data
directory = f"../Parsed_rinex_data/{date}"

cwd = os.getcwd()

if not os.path.exists(directory):
    exit()

# create demon for each json
for file_name in os.listdir(directory):
    if file_name[-5:] == ".json":
        demon = f"""[Unit]
Description=Demon to send data to data flow
After=multi-user.target

[Service]
User=root
Group=root
Type=simple
Restart=always
ExecStart={cwd}/../.venv/bin/python3 {cwd}/send_data.py {start_date} {cwd + "/" + directory + "/" + file_name} {file_name[:4]}

[Install]
WantedBy=multy-user.target"""

        # create demon file
        f = open(demons_directory + '/' + start_date.strftime('%Y-%m-%d') + '99' + file_name[:-5] + '.service', "w")
        f.write(demon)
        f.close()

        # start demon
        # enable demon
        shell_command = 'systemd enable ' + start_date.strftime('%Y-%m-%d') + '99' + file_name[:-5] + '.service'
        os.system(shell_command)

        # reload demons
        shell_command = "systemctl daemon-reload"
        os.system(shell_command)

        # start demon
        shell_command = 'systemctl start ' + start_date.strftime('%Y-%m-%d') + '99' + file_name[:-5] + '.service'
        os.system(shell_command)





