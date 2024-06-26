import time
import paho.mqtt.client as mqtt_client
import random
import sys

if (len(sys.argv)>1): # если запуск из консоли
    print(sys.argv)
else: # если запуск без аргументов консоли
    print(2)

#   брокер, который будет принимать данные
broker = "copift.ru"

#   подключаем клиента по логину и паролю, навешиваем обработчики
client = mqtt_client.Client('isu')
client.username_pw_set("lena", "321")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#   начало работы
print("Connecting to broker", broker)
print(client.connect(broker))
client.loop_start()
print("Publishing")

#    заменить цикл фор на проход джсона по ключам
for i in range(10):
    state = "Данные для отправки "
    state = state + str(random.randint(1,20)) #   рандомное число, чтобы видеть, что данные разные
    print(f"State is {state}") #   выводим в консоль то, что отправили
    client.publish("station_name", state)
    time.sleep(2) #   заснули и следующие данные отправили через 2 секунды

#   закончили отправку
client.disconnect()
client.loop_stop()