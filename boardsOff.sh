#!/bin/sh
. /home/nuphase/scripts/SPIOff.sh
echo out > /sys/class/gpio/gpio47/direction
echo 0 > /sys/class/gpio/gpio47/value
echo out > /sys/class/gpio/gpio46/direction
echo 0 > /sys/class/gpio/gpio46/value

