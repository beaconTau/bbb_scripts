#!/bin/sh
echo out > /sys/class/gpio/gpio60/direction
echo 0 > /sys/class/gpio/gpio60/value
