#!/bin/sh

. ~/scripts/SPIOff.sh

echo 0 > /sys/class/gpio/gpio47/value
echo 0 > /sys/class/gpio/gpio46/value

python ~/scripts/fuse.py adc off

echo 'boards off'

echo 'turning off RF.'

python ~/scripts/fuse.py ant off
sleep 1

python ~/scripts/fuse.py fe off
sleep 1
echo ''
echo 'all off, printing status:'
echo ''
python ~/scripts/status.py
