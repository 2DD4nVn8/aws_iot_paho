import paho.mqtt.client as mqtt
import struct
import ast



MQTT_BROKER_ADDR = '172.29.156.95'
MQTT_BROKER_PORT = 1883





def onConnect(publisher, user_data, flags, response_code):
	print("response code: {0}".format(response_code))
	publisher.subscribe("#", 0)



def onMessage(publisher, user_data, msg):
	print("topic: " + msg.topic)
	print("subtopic " + msg.topic.split("/")[1])
	print("payload: " + str(msg.payload.decode('utf-8')))
	print()



if __name__ == '__main__':
	mqtt_subscriber = mqtt.Client(protocol=mqtt.MQTTv31)
	mqtt_subscriber.on_connect = onConnect
	mqtt_subscriber.on_message = onMessage
	mqtt_subscriber.connect(host=MQTT_BROKER_ADDR, port=MQTT_BROKER_PORT, keepalive=0)

try:
    mqtt_subscriber.loop_forever()
except KeyboardInterrupt:
	None
