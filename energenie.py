import RPi.GPIO as GPIO
from time import sleep

bit1 = 11
bit2 = 15
bit3 = 16
bit4 = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(bit1, GPIO.OUT)
GPIO.setup(bit2, GPIO.OUT)
GPIO.setup(bit3, GPIO.OUT)
GPIO.setup(bit4, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, False)
GPIO.output(18, False)

GPIO.output(bit1, False)
GPIO.output(bit2, False)
GPIO.output(bit3, False)
GPIO.output(bit4, False)

on =  ['1011', '0111', '0110', '0101', '0100']
off = ['0011', '1111', '1110', '1101', '1100']

def change_plug_state(socket, on_or_off):
    state = on_or_off[socket][-1] == '1'
    GPIO.output(bit1, state)
    state = on_or_off[socket][-2] == '1'
    GPIO.output(bit2, state)
    state = on_or_off[socket][-3] == '1'
    GPIO.output(bit3, state)
    state = on_or_off[socket][-4] == '1'
    GPIO.output(bit4, state)
    sleep(0.1)
    GPIO.output(22, True)
    sleep(0.25)
    GPIO.output(22, False)

while True:
    raw_input('Hit any key to turn on: ')
    print('turning on')
    change_plug_state(2, on)
    raw_input('Hit any key to turn off: ')
    print('turning off')
    change_plug_state(0, off)
