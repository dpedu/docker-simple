FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y python3-pip cron && \
    pip3 install simp_le-client && \
    find /etc/cron* -type f -delete && \
    useradd simplecert && \
    touch /etc/crontab

ADD start /start
ADD simplewrapper.py /usr/local/bin/simplewrapper.py
ADD crontab /etc/cron.d/

RUN chmod +x /start /usr/local/bin/simplewrapper.py && \
    chmod 644 /etc/cron.d/crontab

ENTRYPOINT ["/start"]

VOLUME /srv/acme/webroot/.well-known/acme-challenge/
VOLUME /srv/acme/conf/
