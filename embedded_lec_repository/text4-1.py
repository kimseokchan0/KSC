import RPi.GPIO as GPIO
import time

light = [37, 36, 40, 38]


GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT) #GP26이 보드에선 37번
GPIO.setup(36,GPIO.OUT) #GP16이 보드에선 36번
GPIO.setup(40,GPIO.OUT) #GP21이 보드에선 40번
GPIO.setup(38,GPIO.OUT) #GP20이 보드에선 38번

while True: #계속 반복
 for i in range(4) : #i가 0부터 3까지 반복한다.
     GPIO.output(light[i],GPIO.HIGH) #켜졌다가
     time.sleep(0.5) #0.5초 간격
     GPIO.output(light[i],GPIO.LOW) #꺼졌다가
     time.sleep(0.5) #0.5초 간격