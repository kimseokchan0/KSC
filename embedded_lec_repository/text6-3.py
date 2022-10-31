from pickle import BININT1
import RPi.GPIO as GPIO
import time



sw = [5, 6, 13, 19] #스위치 번호
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(sw[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #스위치 4개 초기설정
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
R_Motor = GPIO.PWM(PWMB,500)
L_Motor.start(0)
R_Motor.start(0)

def left_go(): #왼쪽으로 가게하는 함수
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(0)

def right_go(): #오른쪽으로 가게하는 함수
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1) 
    R_Motor.ChangeDutyCycle(0)

def straight(): #앞으로 가게하는 함수
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)       
    R_Motor.ChangeDutyCycle(0)
    L_Motor.ChangeDutyCycle(0)

def back(): #뒤로 가게하는 함수
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)       
    R_Motor.ChangeDutyCycle(0)
    L_Motor.ChangeDutyCycle(0)



try:
    while True:
        if GPIO.input(sw[0]): #스위치1번이 눌렸을때
            straight()
        elif GPIO.input(sw[1]): #스위치2번이 눌렸을때
            left_go()
        elif GPIO.input(sw[2]): #스위치3번이 눌렸을때
            right_go()
        elif GPIO.input(sw[3]): #스위치4번이 눌렸을때
            back()
            


except KeyboardInterrupt:
    pass

GPIO.cleanup()