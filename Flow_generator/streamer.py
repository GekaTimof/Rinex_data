import time
import paho.mqtt.client as mqtt_client
import random
import sys

# test data
# broker address
broker = "copift.ru"
# client data
client = mqtt_client.Client('isu')
client.username_pw_set("lena", "321")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client.on_connect = on_connect

# start proses of sending data
print("Connecting to broker", broker)
print(client.connect(broker))
client.loop_start()
print("Publishing")


state = "Данные для отправки "
state = state + str(random.randint(1,20)) #   рандомное число, чтобы видеть, что данные разные
print(f"State is {state}") #   выводим в консоль то, что отправили
client.publish("station_name", state)
time.sleep(2) #   заснули и следующие данные отправили через 2 секунды


# end proses of sending data
client.disconnect()
client.loop_stop()