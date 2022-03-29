import mediapipe as mp
import cv2
# import streamlit as st
import time
import numpy as np
import HandTrack as ht
import math
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
Volrange=volume.GetVolumeRange()
# print(Volrange)
# st.title("Volume Control Gesture")
# WebCam=st.checkbox("WebCam")
# Volflag=st.checkbox("Enable Volume access")

minVol=Volrange[0]
maxVol=Volrange[1]


cap=cv2.VideoCapture(0)
wCam,hCam = 1000,720
# FRAME_WIN=st.image([])
cap.set(3,wCam)
cap.set(4,hCam)
ptime=0

detector=ht.handdetector(maxdetectionConfidence=0.7,maxHands=1)

Vol=0
volBar=400
volPer=0



colorvol=(255,0,0)
# class Volume():
#     def __init__(self) -> None:
#         pass

    
while True:
    success,img=cap.read()
    img=detector.Findhands(img)
    lmlist,bbox=detector.findPosition(img,draw=True)
    # fingers=detector.fingerUp()
    if len(lmlist)!=0:
        # print(lmlist[4],lmlist[8])
        # filters
        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        # print(area)
        if 150<area<1000:
            length,img,lineinfo=detector.findDistance(4,8,img)
            length1,img,lineinfo=detector.findDistance(8,12,img,color=(255, 238, 0))


            # if length<30:
            #     cv2.circle(img,(lineinfo[4],lineinfo[5]),8,(0,255,0),cv2.FILLED)   #midpoint
            if length>200:                                  #length == volper
                cv2.line(img,(lineinfo[0],lineinfo[1]),(lineinfo[2],lineinfo[3]),(0,0,255),2)
            # hand range 40 - 170
            # Vol range -65 - 0
            # vol=np.interp(length,[20,160],[minVol,maxVol])
            volBar=np.interp(length,[20,160],[400,100])
            volPer=np.interp(length,[20,200],[0,100])#200=length
            # smooth
            smoothness=2
            volPer=smoothness*round(volPer/smoothness)
            fingers=detector.fingerUp()
            # print(length1)
            if length1<35:
                volume.SetMasterVolumeLevelScalar(volPer/100, None)
                cv2.circle(img,(lineinfo[4],lineinfo[5]),8,(0,255,0),cv2.FILLED)    
                colorvol=(0,255,0)
                time.sleep(0.15)
            else:
                colorvol=(255, 238, 0)
            # print(int(length),vol)
        
            # Access the pc volume
            # -------------------------------------------
            # if fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
            # volume.SetMasterVolumeLevel(vol, None)   
            # ---------------------------------------------
            # if fingers[4]==0:
            #     volume.SetMasterVolumeLevel(vol, None)   
    cv2.rectangle(img,(30,100),(85,400),(255,0,0),3)  #drawing volume bar
    cv2.rectangle(img,(30,int(volBar)),(85,400),(255,0,0),cv2.FILLED) #drawing filled bar
    cv2.putText(img,f'{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cvol=int(volume.GetMasterVolumeLevelScalar()*100)
    cv2.putText(img,f'Volume set:{int(cvol)}',(400,50),cv2.FONT_HERSHEY_COMPLEX,1,colorvol,2)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime

    cv2.putText(img,f'fps:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow('VolumeControl',img)
    # frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # FRAME_WIN.image(frame)
    # # print("running...")
    
    
    if cv2.waitKey(1) == ord('q'):
        break
# else:
#     st.write("stop")
cv2.destroyAllWindows()
# print("stopped")

# -----------------------------------------------------------------------------------------

# import mediapipe as mp
# import cv2
# # import streamlit as st
# import time
# import numpy as np
# import HandTrack as ht
# import math
# from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


# import tkinter as tk
# from PIL import Image, ImageTk

# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volume.GetMute()
# # volume.GetMasterVolumeLevel()
# Volrange=volume.GetVolumeRange()
# # print(Volrange)
# # st.title("Volume Control Gesture")
# # WebCam=st.checkbox("WebCam")
# # Volflag=st.checkbox("Enable Volume access")

# minVol=Volrange[0]
# maxVol=Volrange[1]


# cap=cv2.VideoCapture(0)
# # wCam,hCam = 1000,720
# # # FRAME_WIN=st.image([])
# # cap.set(3,wCam)
# # cap.set(4,hCam)
# top = tk.Tk()
# lmain = tk.Label(top,text="AI")
#     # lmain.config(height=900,width=900)
# lmain.pack()
# ptime=0

# detector=ht.handdetector(maxdetectionConfidence=0.7,maxHands=1)

# Vol=0
# volBar=400
# volPer=0



# colorvol=(255,0,0)
# # class Volume():
# #     def __init__(self) -> None:
# #         pass

    
# def show_frame(ptime=0):
#     Vol=0
#     volBar=400
#     volPer=0


#     colorvol=(255,0,0)
#     success,img=cap.read()
#     img=detector.Findhands(img)
#     lmlist,bbox=detector.findPosition(img,draw=True)
#     # fingers=detector.fingerUp()
#     if len(lmlist)!=0:
#         # print(lmlist[4],lmlist[8])
#         # filters
#         area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
#         # print(area)
#         if 150<area<1000:
#             length,img,lineinfo=detector.findDistance(4,8,img)
#             length1,img,lineinfo=detector.findDistance(8,12,img,color=(255, 238, 0))


#             # if length<30:
#             #     cv2.circle(img,(lineinfo[4],lineinfo[5]),8,(0,255,0),cv2.FILLED)   #midpoint
#             if length>200:                                  #length == volper
#                 cv2.line(img,(lineinfo[0],lineinfo[1]),(lineinfo[2],lineinfo[3]),(0,0,255),2)
#             # hand range 40 - 170
#             # Vol range -65 - 0
#             # vol=np.interp(length,[20,160],[minVol,maxVol])
#             volBar=np.interp(length,[20,160],[400,100])
#             volPer=np.interp(length,[20,200],[0,100])#200=length
#             # smooth
#             smoothness=2
#             volPer=smoothness*round(volPer/smoothness)
#             fingers=detector.fingerUp()
#             # print(length1)
#             if length1<35:
#                 volume.SetMasterVolumeLevelScalar(volPer/100, None)
#                 cv2.circle(img,(lineinfo[4],lineinfo[5]),8,(0,255,0),cv2.FILLED)    
#                 colorvol=(0,255,0)
#                 time.sleep(0.15)
#             else:
#                 colorvol=(255, 238, 0)
#             # print(int(length),vol)
        
#             # Access the pc volume
#             # -------------------------------------------
#             # if fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
#             # volume.SetMasterVolumeLevel(vol, None)   
#             # ---------------------------------------------
#             # if fingers[4]==0:
#             #     volume.SetMasterVolumeLevel(vol, None)   
#     cv2.rectangle(img,(30,100),(85,400),(255,0,0),3)  #drawing volume bar
#     cv2.rectangle(img,(30,int(volBar)),(85,400),(255,0,0),cv2.FILLED) #drawing filled bar
#     cv2.putText(img,f'{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
#     cvol=int(volume.GetMasterVolumeLevelScalar()*100)
#     cv2.putText(img,f'Volume set:{int(cvol)}',(400,50),cv2.FONT_HERSHEY_COMPLEX,1,colorvol,2)

#     ctime=time.time()
#     fps=1/(ctime-ptime)
#     ptime=ctime

#     cv2.putText(img,f'fps:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
#     # cv2.imshow('VolumeControl',img)
#     # frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     # FRAME_WIN.image(frame)
#     # # print("running...")
    
#     # cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # img = Image.fromarray(cv2image)
#     # imgtk = ImageTk.PhotoImage(image=img)
#     # lmain.imgtk = imgtk
#     # lmain.configure(image=imgtk)
#     # lmain.after(10, show_frame)
#     return img
    
#     # if cv2.waitKey(1) == ord('q'):
#     #     break
# # else:
# #     st.write("stop")
# # cv2.destroyAllWindows()
# # print("stopped")
# # show_frame(ptime)
# top.mainloop()
