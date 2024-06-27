import time
import paho.mqtt.client as mqtt_client

broker="copift.ru"
client = mqtt_client.Client("admin")
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def on_message(client, userdata, message):
    with open("data-file.txt", "a") as f:
        time.sleep(1)
        data = str(message.payload.decode("utf-8"))
        f.write(data + '\n')
        print("received message =", data)
        f.close()

client.on_message=on_message
client.on_connect=on_connect
client.username_pw_set("admin", "123")

#   начало работы
print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Subcribing")
client.subscribe("station_name")

time.sleep(1800)
client.disconnect()
client.loop_stop()