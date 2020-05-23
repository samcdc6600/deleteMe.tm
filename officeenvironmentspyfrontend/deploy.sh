#!/bin/sh
javac FrontEndClient.java
yes | gcloud app deploy app.yaml index.yaml
echo "Copying resources to backend server."
#scp -i ~/UNI/sem6/cloudComputing/assignments/a2/officeEnvironmentSpyBackend___Keypair.pem BackEndServer.java ubuntu@ec2-52-90-192-10.compute-1.amazonaws.com:BackEndServer.java
scp -i ~/UNI/sem6/cloudComputing/assignments/a2/officeEnvironmentSpyBackend___Keypair.pem BackEndServer.py ubuntu@ec2-52-90-192-10.compute-1.amazonaws.com:BackEndServer.py
echo "Connecting to backend server..."
ssh -i ~/UNI/sem6/cloudComputing/assignments/a2/officeEnvironmentSpyBackend___Keypair.pem ubuntu@ec2-52-90-192-10.compute-1.amazonaws.com <<"ENDSSH"
# echo "Killing java processes."
# sudo pkill -9 java
# echo "Compiling *.java file/s to bytecode target."
# javac BackEndServer.java
# echo "Starting backend server in background"
# java BackEndServer &
# echo "Dissconnecting from backend server."

echo "Killing python processes."
sudo pkill -9 python
echo "Starting backend server in background"
python BackEndServer.py &
echo "Dissconnecting from backend server."
ENDSSH
echo "Done."
