#!/bin/sh

docker build -t pycat docker
docker run -it -v `pwd`:/home/pycat/pycat -e MODULE="${1:-client}" -e ARG="$2" pycat
