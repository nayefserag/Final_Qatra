#!/bin/bash

echo "Clearing out the app directory"
sudo rm -rf /home/ubuntu/qatra-backend

echo "Cloning the app"
sudo cp -r /home/ubuntu/qatra-backend-repo /home/ubuntu/qatra-backend

echo "copy secrets to api app directory"
sudo cp -r /home/ubuntu/secrets/.env /home/ubuntu/qatra-backend/.env

echo "Changing ownership of the app directory"
sudo chown -R ubuntu:ubuntu /home/ubuntu/qatra-backend

echo "Installing dependencies"
cd /home/ubuntu/qatra-backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

