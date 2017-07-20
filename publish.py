#Generate a random number in file is named 'deger'.
#MQTT is using port 1883

# coding: utf-8
#!/usr/bin/env python
import os
import sys
import paho.mqtt.client as mqtt
import time
import random

user="username"
passwd="userpassword"
broker="broker_adres"
port=1883


def on_connect(client,userdata,flags,rc):
  if rc==0:
    print ("succesful connection")
  else:
    print ("bad connection")
    client.loop()


def on_publish(client,userdata,mid):
  print ("message published")

def deger():
    f=open("deger",'w')
    sicaklik=random.randrange(20,40,1)
    f.write(str(sicaklik))
    pub=client.publish("test/test",int(sicaklik),1)
    print ("Publish return : ",pub)
    f.close()


client=mqtt.Client()
client.username_pw_set(user, password=passwd)
client.on_connect=on_connect
client.on_publish=on_publish
client.connect(broker,port)
client.loop_start()

time.sleep(3)
while True:
  deger()
  time sleep(1)
