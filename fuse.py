import os
import time

'''
enable/disable power to subsystems using TPS25940 eFuse
'''

fuse_pin = {0    :   'gpio44',
            1    :   'gpio68',
            2    :   'gpio69',
            3    :   'gpio45',
            }

fuse_id = {'fe'  :   0,
           'ant' :   1,
           'adc' :   2,
           'aux' :   3,
           }

path = '/sys/class/gpio/'

def turnOn(ch):
    '''turn on fuse
    '''
    os.system('echo 1 > '+path+fuse_pin[ch]+'/value')

def turnOff(ch):
    '''turn off fuse
    '''
    os.system('echo 0 > '+path+fuse_pin[ch]+'/value')

def turnOnAll():
    '''turn on all fuses
    '''
    
    for i in range(4):
        turnOn(i)
        time.sleep(0.1)

def turnOffAll():
    '''turn off all fuses
    '''

    for i in range(4):
        turnOff(i)
        time.sleep(0.1)



if __name__=='__main__':
    import status
    import sys

    
    if len(sys.argv) != 3:
        print 'usage: requires 2 arguments: [fuse_id or \'all\'] [\'on\' or \'off\']'
        print 'fuse_id = \'fe\', \'ant\', \'adc\', \'aux\''
        print
        sys.exit(1)

    if sys.argv[1] == 'all':
        if sys.argv[2] == 'on' or sys.argv[2] == '1':
            turnOnAll()
        elif sys.argv[2] == 'off' or sys.argv[2] == '0':
            turnOffAll()
        else:
            print 'invalid setting, nothing was done'
            sys.exit(1)

        time.sleep(0.5)
        status.getCurrents()
        sys.exit(0)

    else:
        try:
            ch = fuse_id[sys.argv[1]]
        except:
            print 'invalid fuse id, nothing was done'
            sys.exit(1)

        if sys.argv[2] == 'on' or sys.argv[2] == '1':
            turnOn(ch)    
        elif sys.argv[2] == 'off' or sys.argv[2] == '0':
            turnOff(ch)
        else:
            print 'invalid stting, nothing was done'
            sys.exit(1)

        time.sleep(0.5)
        status.getCurrents()
        sys.exit(0)
        
