
import RPi.GPIO as GPIO
import time

sw = [5, 6, 13, 19] #스위치 번호
num = [0, 0, 0, 0] #스위치 눌린 횟수

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4): #스위치 4개 초기설정
    GPIO.setup(sw[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


def func(a):
    num[a]+=1 #몇번 눌렸는지 누적횟수
    print("sw" , (a+1) , "click" , num[a]) #몇번 스위치가 몇번 눌렸는지
    time.sleep(0.5)

try:
    while (True):
        for i in range(4):
            if GPIO.input(sw[i]): #만약 스위치가 눌렸으면
                func(i) #아래 함수 실행
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()