FROM debian:latest
# Update the system and install NUT and clean
RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends\
        nut=2.8.1-4 \
        nut-snmp=2.8.1-4 \
        nut-xml=2.8.1-4 \
        usbutils=1:014-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


EXPOSE 3493
# Run the ups driver, ups daemon, and ups monitor
USER root
CMD /sbin/upsdrvctl -u root start && /usr/sbin/upsd && /usr/sbin/upsmon -D
