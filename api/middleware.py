import serial
import time

def dispenseItem(__id, quantity):
    # TODO: Dispensing code goes here
    print(f'Item id: {__id}', f'Quantity: {quantity}')






# print("vending product in slot 51")
# print("opening serial COM4..")

# ser = serial.Serial('COM4', 115200, timeout=1)
# input = "<01C133CD>"
# print(input)

# packet = bytes(input,'ascii')
# print(packet, '\n')
# print('writing bytes:',ser.write(packet),'\n')

# ser.flush()
# time.sleep(5)
# print(ser.readline())
# ser.close()