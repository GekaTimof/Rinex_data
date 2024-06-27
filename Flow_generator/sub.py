import time
import paho.mqtt.client as mqtt_client
import sys

if (len(sys.argv)>1): # если запуск из консоли
    print(sys.argv)
else: # если запуск без аргументов консоли
    print(2)

#   подключаем клиента по логину и паролю, навешиваем обработчики
broker="copift.ru"
client = mqtt_client.Client("admin")
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)
client.on_message=on_message
client.on_connect=on_connect
client.username_pw_set("admin", "123")

#   начало работы
print("Connecting to broker",broker)
client.connect(broker)
client.loop_start()
print("Subcribing")
client.subscribe("ALBH")

#   ждет 30 минут, не придут ли еще данные, затем выключается
time.sleep(1800)
client.disconnect()
client.loop_stop()