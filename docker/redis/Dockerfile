FROM ubuntu:14.04.2

RUN DEBIAN_FRONTEND="noninteractive" apt-get update -y && \
    apt-get install -y -q software-properties-common && \
    add-apt-repository ppa:chris-lea/redis-server && \
    apt-get update -y && \
    apt-get install -y -q redis-server && \
    rm -rf /var/lib/apt/lists/*

COPY redis.conf /etc/redis/redis.conf

EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
