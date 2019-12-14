import os
import ctypes
import time

PATH = 'C:/Users/acer/Downloads/wall/'

SPI=20

def changeBG(path):
    """Change background depending on bit size"""
    count=0
    for x in os.listdir(PATH):
        while True:
            ctypes.windll.user32.SystemParametersInfoW(SPI, 0, PATH+x, 3)
            time.sleep(1)
            count += 1
            break
    changeBG(PATH)
changeBG(PATH)
