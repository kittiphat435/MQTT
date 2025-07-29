from umqtt.simple import MQTTClient
import network
import time
import ubinascii
import machine

# สร้าง unique client ID
client_id = 'clientId-Receiver' + ubinascii.hexlify(machine.unique_id()).decode()

# เชื่อมต่อ WiFi
ssid = 'kru-m'
password = '00000000'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig())

# ฟังก์ชันรับข้อความ
def on_message(topic, msg):
    print('-' * 40)
    print('ได้รับข้อความใหม่:')
    print('Topic:', topic.decode())
    print('ข้อความ:', msg.decode())
    print('-' * 40)

# เชื่อมต่อ MQTT
mqtt = MQTTClient(client_id, 'broker.hivemq.com')
mqtt.set_callback(on_message)
mqtt.connect()
print('เชื่อมต่อ MQTT Broker แล้ว')

# Subscribe topic
topic = b'teachable/dog_detection'
mqtt.subscribe(topic)
print('Subscribe topic:', topic.decode())
print('รอรับข้อความ...')

while True:
    mqtt.check_msg()
    time.sleep(1)

