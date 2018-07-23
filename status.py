#import Adafruit_BBIO.ADC as ADC 
import sys
import subprocess

#BeagleBone ADC pin assignments (needed if using Adafruit_BBIO reader):
ADC_TEMP_PIN_0 = "P9_39"
ADC_TEMP_PIN_1 = "P9_37"
BRD_TEMP_PIN = "P9_35"
FE_IMON_PIN = "P9_36"
ADC_IMON_PIN = "P9_38"
AUX_IMON_PIN = "P9_33"
ANT_IMON_PIN = "P_40"

#ADC number:
ADC_TEMP_0 = 0 #'AIN0'
ADC_TEMP_1 = 2 #'AIN2'
BRD_TEMP = 6 #'AIN6'
FE_IMON = 5 #'AIN5'
ADC_IMON = 3 #'AIN3'
AUX_IMON = 4 #'AIN4'
ANT_IMON = 1 #'AIN1'

path = '/sys/bus/iio/devices/iio:device0/'
adc_range = 4096. #12 bits

def getADCValue(adc_id):
        '''get raw ADC value
        '''
        retv = 1.8  * int(subprocess.check_output(['cat', path+'in_voltage'+str(adc_id)+'_raw'])) / adc_range #volts
        return retv

def getTemperatures(terminal_print=True):
        '''read board temperatures
        '''
        factor = 1.5 #from voltage divider
        
        volts_board_0 = factor * getADCValue(ADC_TEMP_0)
        volts_board_1 = factor * getADCValue(ADC_TEMP_1)
        volts_controller_board = factor * getADCValue(BRD_TEMP)

        ## here is the linear-approximate response (see TMP20 datasheet for more info)
	temp_adc_0 = int((volts_board_0-1.8583)/(-0.01167))
        temp_adc_1  = int((volts_board_1-1.8583)/(-0.01167))
        temp_cntrl = int((volts_controller_board-1.8583)/(-0.01167))

        if terminal_print:
                print '-----'
                print 'board temperatures:'
                print 'adc board 0:      ', temp_adc_0, 'C'
                print 'adc board 1:      ', temp_adc_1, 'C [probably not connected in protoBEACON]'
                print 'controller board: ', temp_cntrl, 'C'
                
	return temp_adc_0, temp_adc_1, temp_cntrl

def getCurrents(terminal_print=True):
        '''read fuse currents
        '''
        imon_res = 6800.e-6 #Mohms
        imon_gain = 52.0 #uA/A
        imon_ofst = 0.8 #uA

        #get current in mA
        cur_fe = int(1000 * (getADCValue(FE_IMON)/imon_res - imon_ofst) / imon_gain)
        cur_adc= int(1000 * (getADCValue(ADC_IMON)/imon_res - imon_ofst) / imon_gain)
        cur_ant= int(1000 * (getADCValue(ANT_IMON)/imon_res - imon_ofst) / imon_gain)
        cur_aux= int(1000 * (getADCValue(AUX_IMON)/imon_res - imon_ofst) / imon_gain)

        if terminal_print:
                print '-----'
                print 'system power consumption:'
                print 'ant FEE        :', cur_ant, 'mA'
                print '2nd stage amps :', cur_fe, 'mA'
                print 'ADC board      :', cur_adc, 'mA'
                print 'aux plug       :', cur_aux, 'mA'

        return cur_fe, cur_adc, cur_ant, cur_aux

if __name__=="__main__":
        
        getTemperatures()
        getCurrents()
