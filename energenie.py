import RPi.GPIO as GPIO
from time import sleep

# The GPIO pins for the Energenie module
BIT1 = 11
BIT2 = 15
BIT3 = 16
BIT4 = 13

ON_OFF_KEY = 18
ENABLE = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(BIT1, GPIO.OUT)
GPIO.setup(BIT2, GPIO.OUT)
GPIO.setup(BIT3, GPIO.OUT)
GPIO.setup(BIT4, GPIO.OUT)

GPIO.setup(ON_OFF_KEY, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)

GPIO.output(ON_OFF_KEY, False)
GPIO.output(ENABLE, False)

GPIO.output(BIT1, False)
GPIO.output(BIT2, False)
GPIO.output(BIT3, False)
GPIO.output(BIT4, False)

# Codes for switching on and off the sockets
#        all     1       2       3       4
ON  = ['1011', '1111', '1110', '1101', '1100']
OFF = ['0011', '0111', '0110', '0101', '0100']

def change_plug_state(socket, on_or_off):
    state = on_or_off[socket][3] == '1'
    GPIO.output(BIT1, state)
    state = on_or_off[socket][2] == '1'
    GPIO.output(BIT2, state)
    state = on_or_off[socket][1] == '1'
    GPIO.output(BIT3, state)
    state = on_or_off[socket][0] == '1'
    GPIO.output(BIT4, state)
    sleep(0.1)
    GPIO.output(ENABLE, True)
    sleep(0.25)
    GPIO.output(ENABLE, False)

def switch_on(socket):
    change_plug_state(socket, ON)

def switch_off(socket):
    change_plug_state(socket, OFF)
