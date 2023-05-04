#!/bin/bash

cd /home/ubuntu/qatra-backend

echo "starting server"
sudo -E bash -c "source env/bin/activate; pm2 start server.json; pm2 save"
