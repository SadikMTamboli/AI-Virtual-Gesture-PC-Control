import os
import mediapipe as mp
import cv2 
import time
from pyautogui import sleep
import HandTrack as ht
import pyautogui as pg
import load
print("\n")
print("Welcome To AI Virtual Gesture PC Control".center(210,'-'),"\n")

print("Choose your option:".center(210),"\n")
print("1:Volume Access".center(210),"\n\n","2:Mouse Access".center(210),"\n\n","3:Keyboard Access".center(210),"\n\n","4:Terminate".center(210))
while(1):
    # print(">>".center(210))
    n=int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t>>"))

    if n==1:
        # print("\t\t\t\t\tThis will take a moment...")
        sleep(1)
        
        load.loading('Volume')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VolumeControl.py')
        
    elif n==2:
        load.loading('Mouse')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualMouse.py')
        # sleep(0.5)
    elif n==3:
        load.loading('Keyboard')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualKeyboard.py')
        sleep(0.5)
    elif n==4:
        load.loading('Closing')
        sleep(0.3)
        break
    else:
        print("INVALID".center(210))
        sleep(0.5)

