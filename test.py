from firebase.api import RTDB

db = RTDB()


#LISTEN
# @db.ignore_first_call
# def listen_token(event):
#     print(event.data)

# db.listen('/token', listen_token)


# READ
# print(db.read('/'))

# UPDATE
# db.update('/', {
#     'token': 10
# })

#RASPI SEND COMMAND
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)
# PIN = 7

# GPIO.setup(PIN, GPIO.OUT)

# while True:
#     GPIO.output(PIN, GPIO.HIGH)
#     sleep(1)
#     GPIO.output(PIN, GPIO.LOW)
#     sleep(1)
