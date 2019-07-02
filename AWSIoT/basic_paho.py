#!/usr/bin/python

# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import ast
import json
import os
import logging

# read AWS parametars json
json_path = "/home/pi/WorkSpace/IoT_test/AWS_IoT.txt"
connect_json = open(json_path,'r')
connect_dict = json.load(connect_json)

# AWS parameters 
awshost = connect_dict["ENDPOINT"]      
awsport = 8883                                              
clientId  = "IoT_test_1"                             
thingName = "IoT_test"                            
caPath = "root-CA.crt"                               
certPath = "IoT_test.cert.pem"                            
keyPath = "'IoT_test.private.key'"                         
mode='both'
pub_message='Hello World!'
SUB_topic="#"

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Custom MQTT message callback
def on_message(client, userdata, message):
    print("--------------")
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n")

def on_connect(client, userdata, flags, rc):                # func for making connection
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(SUB_TOPIC , 1)  

def on_log(client, userdata, level, msg):
    print(msg.topic+" "+str(msg.payload))

# Publish to the same topic in a loop forever
loopCount = 0
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
mqttc.on_log = on_log
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)      # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60*10)               # connect to aws server
 
mqttc.loop_forever()                   