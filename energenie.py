import RPi.GPIO as GPIO
from time import sleep

# The GPIO pins for the Energenie module
bit1 = 11
bit2 = 15
bit3 = 16
bit4 = 13

on_off_key = 18
enable = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(bit1, GPIO.OUT)
GPIO.setup(bit2, GPIO.OUT)
GPIO.setup(bit3, GPIO.OUT)
GPIO.setup(bit4, GPIO.OUT)

GPIO.setup(on_off_key, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)

GPIO.output(on_off_key, False)
GPIO.output(enable, False)

GPIO.output(bit1, False)
GPIO.output(bit2, False)
GPIO.output(bit3, False)
GPIO.output(bit4, False)

# Codes for switching on and off the sockets
# the first [0] is all on / off
all_sockets = 0
on  = ['1011', '1111', '1110', '1101', '1100']
off = ['0011', '0111', '0110', '0101', '0100']

def change_plug_state(socket, on_or_off):
    state = on_or_off[socket][3] == '1'
    GPIO.output(bit1, state)
    state = on_or_off[socket][2] == '1'
    GPIO.output(bit2, state)
    state = on_or_off[socket][1] == '1'
    GPIO.output(bit3, state)
    state = on_or_off[socket][0] == '1'
    GPIO.output(bit4, state)
    sleep(0.1)
    GPIO.output(enable, True)
    sleep(0.25)
    GPIO.output(enable, False)

while True:
    raw_input('Hit any key to turn on: ')
    print('Turning on...')
    change_plug_state(2, on)
    raw_input('Hit any key to turn off: ')
    print('Turning off...')
    change_plug_state(all_sockets, off)
