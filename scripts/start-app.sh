#!/bin/bash

cd /home/ubuntu/qatra-backend

echo "starting server"
sudo -E pm2 start server.json
pm2 save
