import RPi.GPIO as GPIO
import time
import random




light= [37, 36, 40, 38]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT) #GP26이 보드에선 37번
GPIO.setup(36,GPIO.OUT) #GP16이 보드에선 36번
GPIO.setup(40,GPIO.OUT) #GP21이 보드에선 40번
GPIO.setup(38,GPIO.OUT) #GP20이 보드에선 38번



random.shuffle(light)

for j in range(4) : #컨트롤 c를 눌러 초기화했음에도 다음번 시작때 초기화가 되지않아
    GPIO.output(light[j],GPIO.LOW) # for문을 사용해 초기화 시켰다.

try :
    for i in range(10) : #10번 반복
        b = 0 #b선언

        if i>3 and i<=7: #light[4]일때 light[0]으로 바꿔주기위해
            b=i-4
        elif i>7: #light[8]일때 light[0]으로 바꿔주기 위해
            b=i-8
        else:
            b=i
            
        GPIO.output(light[b],GPIO.HIGH) #켜기
        time.sleep(0.5) #0.5초 간격
        GPIO.output(light[b],GPIO.LOW) #끄기
        time.sleep(0.5) #0.5초 간격
except:
    GPIO.cleanup() #reset