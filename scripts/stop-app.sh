#!/bin/bash

cd /home/ubuntu/qatra-backend

echo "Stopping server"
pm2 stop server.json