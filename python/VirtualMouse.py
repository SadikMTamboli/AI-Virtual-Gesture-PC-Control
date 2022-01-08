import mediapipe as mp
import cv2
import time
import math
import pyautogui as pg
import numpy as np
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from numpy import true_divide
import HandTrack as ht



pg.FAILSAFE=False
smoothing = 2
plocx,plocy=0,0
clocx,clocy=0,0      
wCam,hCam = 900,500         
frameR=100                 #Frame reduction
cap=cv2.VideoCapture(0)

cap.set(3,wCam)         #size of screen
cap.set(4,hCam)
ptime=0
c,d=0,0
detector=ht.handdetector(maxHands=1)
ptime=0
wScr,hScr= pg.size()
l=[]
f=0
m=0
# print(wScr,hScr)
while True:
    
    success,img=cap.read()
    # img=cv2.flip(img,1)
    img=detector.Findhands(img)
    lmlist,bbox=detector.findPosition(img)
    # cMouseX, cMouseY = pg.position()
    
# get tip of i & t
    if len(lmlist)!=0:
        x1,y1=lmlist[8][1:]
        x2,y2=lmlist[12][1:]

        x3,y3=lmlist[4][1],lmlist[4][2]
        x4,y4=lmlist[8][1],lmlist[8][2]
        # print(x1,y1,x2,y2)
        
        #check fing up
        fingers=detector.fingerUp()
        # print(fingers)
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,0),2)
        
        #only index
        if fingers[1]==1 and fingers[2]==1:
            
            x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            clocx=plocx+(x3-plocx)/smoothing
            clocy=plocy+(y3-plocy)/smoothing
            pg.moveTo(wScr-clocx,clocy)
            cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
            cv2.circle(img,(x2,y2),10,(255,0,0),cv2.FILLED)
            plocx,plocy=clocx,clocy

            length,img,infoline=detector.findDistance(8,12,img)
            cv2.line(img,(infoline[0],infoline[1]),(infoline[2],infoline[3]),(255, 238, 0),2)
            length=length//10
            print(length)
            dragflag=0
            if length==2.0 or length==1.0 or length==0.0 or length==3.0:
                if dragflag==1:
                    dragflag=0
                    pg.mouseUp(button='left')
                    # pg.moveTo(wScr-clocx,clocy)                
                    # pg.dragTo(wScr-clocx,clocy)
                    print("U")
                elif dragflag==0:
                    dragflag=1
                    pg.mouseDown(button='left')
                    x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
                    y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
                    clocx=plocx+(x3-plocx)/smoothing
                    clocy=plocy+(y3-plocy)/smoothing
                    pg.moveTo(wScr-clocx,clocy)
                    cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
                    plocx,plocy=clocx,clocy
                    print("D")
            else:
                pg.mouseUp(button='left')
                print("Else up")
            
                # pg.dragTo(wScr-clocx,clocy,duration=1)
        #only middle
        
        # if fingers[1]==1 and fingers[2]==1:
        #     length,img,infoline=detector.findDistance(8,12,img)
        #     # print(type(length))
        #     # print(length)
        #     # if  length<30:

        #     #     c+=1
        #     #     cv2.circle(img,(infoline[4],infoline[5]),8,(0,255,0),cv2.FILLED)     
            
        #     #     # pg.click()
        #     #     print(length,c)
        #     #     time.sleep(0.15)
        #     pg.scroll(120 if length<30 else -120)
        #         # f=1
        
    
        
        if fingers[1]==0 and fingers[2]==1 :
            c+=1
            print("left click",c)
            
            pg.click()
            time.sleep(0.15)
        if fingers[2]==0 and fingers[1]==1:
            c+=1
            print("right click",c)
            
            pg.rightClick()  
            time.sleep(0.15)
        
        # length,img,infoline=detector.findDistance(8,12,img)
        
        # if length<30:
        #     print(length)
        #     # pg.doubleClick()
        #     # pg.mouseDown()
        #     m=1
        #     x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
        #     y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
        #     clocx=plocx+(x3-plocx)/smoothing
        #     clocy=plocy+(y3-plocy)/smoothing
        #     pg.dragRel(wScr-clocx,clocy,button='left')
        #     cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
        #     plocx,plocy=clocx,clocy
        #     # time.sleep(0.15)
        #     print("D")
            
        # else:
        #     pg.mouseUp()
        
        # if fingers[0]==1:
        #     pg.doubleClick()
        #     pg.mouseDown()
            # pg.moveTo(wScr-clocx,clocy)
        # m=0
        # if fingers[1]==0 and fingers[2]==0:
        #    pg.doubleClick()
        #    pg.mouseDown()
        #    m=1
        #    pg.drag
        # #    time.sleep(0.15)
        #    print("down click")
        # # if fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
        # if m==1:
        #     pg.mouseUp()
        #     print("mouse up")
        #     d+=1
            
        #     pg.hotkey('win','d')
        #         # print("drag",d)
        #         # pg.scroll(-10)
        #     print(d)   
        #     time.sleep(0.15)
        # c=0
        #     if c==0:
        #         pg.hotkey('win','d')
        #         c=1 

        # elif fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
        #     if c==0:
        #         pg.hotkey('win','4')
        #         c=1

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime

    cv2.putText(img,f'fps:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow('VirtualMouse',img)
    
    if cv2.waitKey(1) == ord('q'):
        
        break

cv2.destroyAllWindows()
# https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse/tree/main/src