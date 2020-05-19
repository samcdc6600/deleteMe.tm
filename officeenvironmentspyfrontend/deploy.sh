#!/bin/sh
yes | gcloud app deploy app.yaml index.yaml
scp -i ~/UNI/sem6/cloudComputing/assignments/a2/officeEnvironmentSpyBackend___Keypair.pem BackEndServer.java ubuntu@ec2-52-90-192-10.compute-1.amazonaws.com:BackEndServer.java
ssh -i ~/UNI/sem6/cloudComputing/assignments/a2/officeEnvironmentSpyBackend___Keypair.pem ubuntu@ec2-52-90-192-10.compute-1.amazonaws.com <<"ENDSSH"
pkill java
java BackEndServer.java &
echo "cats"
ENDSSH


