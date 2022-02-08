#!/bin/bash

set -x 

docker-compose up -d
docker exec -it trabalho-rmi python3 server.py