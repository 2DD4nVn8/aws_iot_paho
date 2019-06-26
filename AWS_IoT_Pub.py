import paho.mqtt.client
import ssl
import subprocess
import json
import datetime
import time

endpoint = "**********.amazonaws.com"#AWSのエンドポイント
port = 8883#AWSのポート
PUB_TOPIC = "AWS_SYS/QOL"
rootCA = "root-CA.crt"  #ルート証明書
cert = "aws-iot.cert.pem"  #デバイス証明書
key = "aws-iot.private.key" #keyを設定
clientID = "tester_1"

def on_connect(client, userdata, flags, respons_code):
    print("Connected")
    client.subscribe(SUB_TOPIC)#サブスクライブする

def on_message(client, userdata, msg):
    print(msg)

if __name__ == '__main__':
    client = paho.mqtt.client.Client(clientID)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(ca_certs=rootCA, certfile=cert, keyfile=key, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    client.connect(endpoint, port=port, keepalive=60)
print("StartScript")
client.loop_start()
#client.loop_forever()

while(1):
    time.sleep(2)
    time_now = datetime.datetime.now().strftime("%Y/%m/%dT%H:%M:%S")
    PUB_message = '{"time":"' + time_now + '", "senser_data":100}'
    client.publish(PUB_TOPIC,PUB_message, qos=1)
    print(PUB_message)
