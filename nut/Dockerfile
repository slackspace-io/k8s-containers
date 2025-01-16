FROM debian:latest
# Update the system and install NUT and clean
RUN echo "deb http://deb.debian.org/debian testing main" >> /etc/apt/sources.list
RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends\
        nut \
        nut-snmp \
        nut-xml \
        usbutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#use debian testing


EXPOSE 3493
# Run the ups driver, ups daemon, and ups monitor
USER root

CMD /sbin/upsdrvctl -u root start && /usr/sbin/upsd && /usr/sbin/upsmon -D
