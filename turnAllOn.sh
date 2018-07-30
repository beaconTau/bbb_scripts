#!/bin/sh

python ~/scripts/fuse.py adc on

echo 0 > /sys/class/gpio/gpio47/value
echo 0 > /sys/class/gpio/gpio46/value

echo 1 > /sys/class/gpio/gpio47/value
echo 1 > /sys/class/gpio/gpio46/value
echo 'turning on boards... waiting 30 seconds'
sleep 30
. /home/nuphase/scripts/SPIOn.sh
echo 'boards on'

sleep 1


echo 'turning on RF.'

python ~/scripts/fuse.py fe on
sleep 2

echo 'aligning adcs...'
python ~/nuphase_python/align_adcs.py -m


python ~/scripts/fuse.py ant on
sleep 1
echo 'all on, printing status:'

python ~/scripts/status.py
