import functools
import time
from sys import argv
import schedule
import paho.mqtt.client as mqtt_client
import datetime
import json

# test data
# broker address
broker = "copift.ru"

start_date = "2024-01-01"
link = "/home/evgeniy/PycharmProjects/Rinex_data/Parsed_rinex_data/2024-01-01/ALBH00CAN_R_20240010000_01D_30S_MO.json"
station_name = "ALBH"


# client data
client = mqtt_client.Client('isu')
client.username_pw_set("lena", "321")

# how much day ago we get data
delay = 4

# date - date when we start this script
#start_date = argv[1]
# link - link to file with data we need to send
#link = argv[2]
# station_name - name of station from where we get data
#station_name = [3]

d = datetime.datetime


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
client.on_connect=on_connect


def send_data(client, data, station_name, sending_time):
    data_to_send = json.dumps({"datetime": sending_time, "data": data})
    client.publish(f"{station_name}", data_to_send) #data.insert(0, sending_time)

# start proses of sending data
print("Connecting to broker", broker)
print(client.connect(broker))
client.loop_start()
print("Publishing")

def p(x):
    print(x)

# open json file
with open(link) as json_file:
    data_json = json.load(json_file)

    # send data every 30 second
    schedule.every().minute.at(":00").do(functools.partial(send_data,
                                                client=client,
                                                data=data_json[start_date + d.strftime(d.now(), " %H:%M:00")],
                                                station_name=station_name,
                                                sending_time=start_date + d.strftime(d.now(), " %H:%M:00")))

    schedule.every().minute.at(":30").do(functools.partial(send_data,
                                                client=client,
                                                data=data_json[start_date + d.strftime(d.now(), " %H:%M:30")],
                                                station_name=station_name,
                                                sending_time=start_date + d.strftime(d.now(), " %H:%M:00")))

    while not datetime.datetime.strptime(start_date, "%Y-%m-%d") == datetime.date.today() - datetime.timedelta(days=delay):
        schedule.run_pending()
        time.sleep(1)

# end proses of sending data
client.disconnect()
client.loop_stop()
