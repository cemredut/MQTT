#The values keeping in database
#Using email service and it is using port 587

import paho.mqtt.client as mqttClient
import time
import sys
import smtplib
import os
import string
import MySQLdb
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

user="username"
passwd="userpassword"


host="localhost"
user="root"
passwd=""
db="database_name"

db=MySQLdb.connect(host,user,passwd,db)
cur=db.cursor()


  
def alarm(usr,psw,to,subj,message):
  try:
    msg=MIMEMultipart()
    msg['From']=usr
    msg['To']=to
    msg['Subject']=subj
    msg.attach(MIMEText(message,'plain'))

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(usr,psw)
    text=msg.as_string()
    server.sendmail(usr,to,text)
    server.quit()
    print "Sending mail"
  except Exception as error:
    print "failed to send mail"
    print str(error)
  
  
def on_connect(client, userdata, flags, rc):
  if rc == 0:

    print("Connected to broker")
    global Connected
    Connected = True

  else:
    print("Connection failed")

def on_message(client, userdata, message):
  value=(int(message.payload))
  database(value)
  if value>35:
    usr="sender_email"
    psw="sender_email_passw"
    to="received_email"
    subject="subject"
    msg='Subject:{}\n\n The temperature higher than 35'.format(subject)
    alarm(usr,psw,to,subject,msg)
  else:
    print "normally"

def database(degree_value):
  sql=("""INSERT INTO table_name (attribute) VALUES (%s)""",[degree_value])
  try: 
        print "Write on database"
        cur.execute(*sql)
        db.commit()
  except Exception as error:
        print "Failed"
        print str(error)
Connected = False

broker_address= "broker_adres"
port = 1883

client = mqttClient.Client()
client.username_pw_set(user,password=passwd)
client.on_connect= on_connect 
client.on_message= on_message
client.connect(broker_address, port=port)
client.loop_start()
client.subscribe("test/test")
while True:
  time.sleep(1)
