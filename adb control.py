#Author: Daoma

from ppadb.client import Client as AdbClient
from time import sleep

buttons=['792 453','792 668','792 882','792 1092','792 1313','792 1528','792 1740','792 1955'] #positions of Following/Unfollowing button

def connect():
    client=AdbClient(host="127.0.0.1", port=5037)

    devices  = client.devices()

    if len(devices )==0:
        print ("no devices")
        quit()
    device=devices[0]
    print("here")

    return device, client


if __name__ == '__main__':
    device, client = connect()
    
    while j<number_of_following:
    

        for i in buttons:

            device.shell(f'input tap {i}')
            sleep(.01)

        device.shell(f'input swipe 584 2293 584 563 3000') #if you don't know what you doing don't touch this line
        sleep(.01)
        