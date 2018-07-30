import os
import time
import subprocess

status_file = 'fan_status'

fan_pwm_gpio = 'ehrpwm1\:o'
fan_pow_enable_gpio = 'gpio115'
path = '/sys/class/pwm/'

if __name__=='__main__':
    import sys
    
    if sys.argv[1] == 'on':
        os.system("echo 1 > /sys/class/gpio/gpio115/value")
    elif sys.argv[1] == 'off':
        os.system("echo 0 > /sys/class/gpio/gpio115/value")
        
        
