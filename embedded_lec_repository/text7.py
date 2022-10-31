import threading
import serial
import time
import RPi.GPIO as GPIO




PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
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

def right_go(): #오른쪽으로 가게하는 함수
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)

def straight(): #앞으로 가게하는 함수
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)

def back(): #뒤로 가게하는 함수
    L_Motor.ChangeDutyCycle(100)
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)

def stop(): #모터중지
    L_Motor.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)


bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.1)

gData = "" #전역변수로 사용할 변수

def serial_thread():
    global gData    #전역변수로 선언
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data #시리얼 통신으로 받은 데이터를 전역변수에 할당

def main():
    global gData #전역변수로 선언
    try:
        while True:
            if gData.find("go") >= 0:
                gData=""
                print("up")
                straight()
            elif gData.find("back") >= 0:
                gData=""
                print("back")
                back()
            elif gData.find("left") >= 0:
                gData=""
                print("left")
                left_go()
            elif gData.find("right") >= 0:
                gData=""
                print("right")
                right_go()
            elif gData.find("stop") >= 0:
                gData="" 
                print("stop")
                stop()

    except KeyboardInterrupt:
        pass
  

if __name__ == '__main__' :
    task1 = threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
