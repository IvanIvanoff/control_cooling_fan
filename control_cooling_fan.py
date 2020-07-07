#!/usr/bin/python3

from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time
import datetime

log_file = '/var/log/control_cooling_fan.log'

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
fan_on = False

while(True):
  cpu = CPUTemperature()
  cpu_temp = cpu.temperature
  if cpu_temp > 70 and fan_on == False:
    GPIO.output(17, 1)
    fan_on = True
  elif cpu_temp < 65 and fan_on == True:
    GPIO.output(17, 0)
    fan_on = False

  file_object = open(log_file, 'a')

  datetime_str = datetime.datetime.utcnow().strftime('%d/%m/%y %H:%M:%S')
  file_object.write(f'[{datetime_str}] {cpu_temp}\n')
  file_object.close()
  time.sleep(10)
