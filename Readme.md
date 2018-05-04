============================================================
Continuous and Automated IoT application deployment for For computing
============================================================

This Readme file explains procedure to setup and procedure to deploy IoT applications for Fog architecture.

Please read carefully the original IEEE paper and our implementaion report in IEEE paper format for thorough understanding of concepts and technologies 
before implementing steps below:

1. Setup Concourse.ci server for CI/CD - The URL provided below explains in detail how to install concourse CI/CD tool (I have installed 
Concourse on local VM using vagrant as described in URL below)
URL: https://specify.io/how-tos/concourse-ci-continious-integration-and-delivery-of-microservices#introduction

2. Build the pipeline in YML file as described in URL. I have attached my pipeline YML file,
the only fields need to be edited are in Resources: DockerHub repo, URL, username and password. 
and Tasks: Send cmd to EC2: Docker pull command of DockerHub.

3. push the application to your Github repo and write appropriate Dockerfile for it in pipeline (We have used ultra_test.py as our application file and Dockerfile is present in YML file)

4. Update configuration to server and connect raspberry pi as edge device and manually run mqtt_test.py on it. (Edit this file for your use case,
You can also SSH into pi and run the file remotely)

5. You can subscribe using MQTT protocol in EC2 server to observe sensor data from the pi.


