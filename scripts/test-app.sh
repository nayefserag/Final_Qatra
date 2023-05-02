#!/bin/bash
sleep 10

cd /home/ubuntu/qatra-backend


status_code=$(curl --write-out %{http_code} --silent --output /dev/null localhost:80)

if [[ "$status_code" -ne 200 ]] ; then
    echo "App is not running healthy on localhost:80"
    exit 1
else
    echo "App is running healthy on localhost:80"
    exit 0
fi