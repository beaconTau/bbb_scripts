#!/bin/sh
echo out > /sys/class/gpio/gpio47/direction
echo 1 > /sys/class/gpio/gpio47/value
echo out > /sys/class/gpio/gpio46/direction
echo 1 > /sys/class/gpio/gpio46/value
echo 'turning on boards... waiting 30 seconds'
sleep 30
. /home/nuphase/scripts/SPIOn.sh
echo 'boards on'
