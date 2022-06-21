#This script will Blink the led Hooked up to Pin GPIO448 or Physically at pin number 40 of VisionFive v1.
#if this script executes and led starts to blink then fine otherwise if error regarding to Cronie-anacorn appears the you can install that using
# dnf install cronie cronie-anacorn -y
# For permission denied you can use "sudo" or "sh - " command.
# for pinout and Configuring Gpios you can reffer to "RVSpace.org"

import requests
from time import sleep
import os
path = '/sys/class/gpio'
os.chdir(path)
os.system(f'echo gpio > export')
os.chdir('gpio448')
os.system(f'echo out > direction')

while (1):
    
    os.system(f'echo 1 > value')
    sleep(1)
    os.system(f' echo 0 > value')
    sleep(1)
    print('done')
