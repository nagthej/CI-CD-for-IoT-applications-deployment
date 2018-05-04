import time
import json
import paho.mqtt.client as paho
import subprocess 
import os

broker="ec2-18-221-47-29.us-east-2.compute.amazonaws.com"  #EC2 brocker 

#Callback on receving a message
def on_message(client, userdata, message):
	time.sleep(1)
	print("Received URL to Dockerhub =",str(message.payload.decode("utf-8")))
    url=message.payload.decode("utf-8")
    subprocess.call("docker stop $(docker ps -a -q)",shell= True)   #stop running container
    subprocess.call("docker rm $(docker ps -a -q) --force",shell= True) #remove container
    subprocess.call("docker image rm $(docker image ls -a -q) --force",shell= True) #remove docker image
    subprocess.call("docker run -t --privileged URL",shell= True) #pull and run the latest application
        	
client= paho.Client("client-1") #create client object 

#Bind function to callback
client.on_message=on_message
print("connecting to broker ",broker)
client.connect(broker) #connect to brocker
print("connected to broker ",broker)
client.loop_start() #start loop to process received messages
client.subscribe("URL_hub") #subscribe to message from EC2 server
time.sleep(1)

while True:
      time.sleep(1)          #Wait here for to receive URL from server
client.loop_forever()
