import os
import time
import serial
from api.config import DevelopmentConfig
from api.utils import getItemSlot


def dispenseItem(__id, quantity):
    slot = getItemSlot(__id)
    
    hex_slot = hex(slot)
    command_suffix = str(hex(int('0x100', 16) - slot))
    command = f"<01C1{hex_slot[2:].upper()}{command_suffix[2:].upper()}>"

    try:
        ser = serial.Serial(DevelopmentConfig.COM_PORT, 115200, timeout=1)
        packet = bytes(command,'ascii')
        ser.write(packet)
        ser.flush()
        time.sleep(5)
        response = ser.readline()
        ser.close()

        return 'success' if response == '<0x06>' else 'failure', command
    
    except:
        print(DevelopmentConfig.COM_PORT)
        return 'failure', ''