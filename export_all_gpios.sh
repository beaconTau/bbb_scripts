#! /bin/sh

##GPIO mapping of BBB on phased-array controller board 2018.7
# gpio_40 : fan pwm
# gpio_48 : aux power plug fault indication
# gpio_26 : fe power plug fault indication
# gpio_65 : ant power plug fault indication
# gpio_27 : adc power plug fault indication
# gpio_45 : aux power plug enable
# gpio_44 : fe power plug enable
# gpio_68 : ant power plug enable
# gpio_69 : adc power plug enable
# gpio_22 : heater on/off (or pwm?)
# gpio_49 : gpio to adc board 0
# gpio_117: gpio to adc board 1
# gpio_115: 12V regulator enable (used for fan only)
# gpio_66 : aux0
# gpio_67 : aux1
# gpio_60 : SPI bus enable
# gpio_23 : GPS enable
# gpio_46, gpio_47: adc board full power enable

#export all
for i in 22 23 26 27 44 45 46 47 48 60 65 66 67 68 69 115;
do echo $i > /sys/class/gpio/export 
done

#set boards to off 
for i in 46 47 ; 
do echo low > /sys/class/gpio/gpio$i/direction 
done 

#set fault indicators to input
for i in 26 27 48 65 ;
do echo in > /sys/class/gpio/gpio$i/direction
done

#turn all fuses off
for i in 44 45 68 69
do echo low > /sys/class/gpio/gpio$i/direction
done

#enable gps
echo high > /sys/class/gpio/gpio23/direction

#keep +12V (fan) off
echo low > /sys/class/gpio/gpio115/direction

#setup fan control pin as PWM
#export ehrpwm1=/sys/devices/platform/ocp/48302000.epwmss/48302200.pwm/pwm/pwmchip2
#config-pin P9_14 pwm

#keep SPI bus off
echo high > /sys/class/gpio/gpio60/direction

#turn off heater
echo low > /sys/class/gpio/gpio22/direction




