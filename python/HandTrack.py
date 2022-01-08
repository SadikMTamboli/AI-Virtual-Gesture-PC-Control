import mediapipe as mp
import cv2
import time
import math
import numpy as np

from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from numpy import true_divide

class handdetector():
    def __init__(self,mode=False,maxHands=2,maxdetectionConfidence=0.5,mintrackconfidence=0.5) -> None:
        self.mode=mode
        self.maxHands=maxHands
        self.maxdetectionConfidence=maxdetectionConfidence
        self.mintrackconfidence=mintrackconfidence

        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands(self.mode,self.maxHands,self.maxdetectionConfidence,self.maxdetectionConfidence)
        self.mpDraw=mp.solutions.drawing_utils
        self.tipIds=[4,8,12,16,20]
    def Findhands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handlms,self.mphands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self,img,handNo=0,draw=True):
        
        xList=[]
        yList=[]
        bbox=[]
        self.lmlist=[]
        if self.results.multi_hand_landmarks:
            myhand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                xList.append(cx)
                yList.append(cy)
                # print(id,cx,cy)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),4,(255,0,255),cv2.FILLED)

            xmin,xmax=min(xList),max(xList)
            ymin,ymax=min(yList),max(yList)
            bbox=xmin,ymin,xmax,ymax
            # if draw:
            #     cv2.rectangle(img,(xmin-20,ymin-20),(xmax+20,ymax+20),(0,255,0),2)
            if draw:
                cv2.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[2]+20,bbox[3]+20),(0,255,0),2)
        return self.lmlist,bbox
    def fingerUp(self):
        fingers=[]
#thumb
        if self.lmlist[self.tipIds[0]][1]>self.lmlist[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            #finger
        for id in range(1,5):
            if self.lmlist[self.tipIds[id]][2] < self.lmlist[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    def findDistance(self,p1,p2,img,draw=True,r=15,t=3,color=(255,0,0)):
        x1,y1=self.lmlist[p1][1:]
        x2,y2=self.lmlist[p2][1:]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        if draw:
            cv2.line(img,(x1,y1),(x2,y2),color,t)
            cv2.circle(img,(x1,y1),8,(255,0,255),cv2.FILLED) #index
            cv2.circle(img,(x2,y2),8,(255,0,255),cv2.FILLED)
            cv2.circle(img,(cx,cy),8,(255,0,255),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)

        return length,img,[x1,y1,x2,y2,cx,cy]

    def Volume_Access(self,img,lmlist,minVol,maxVol,volBar,volPer,volume,vol):
        if len(lmlist)!=0:
        # print(lmlist[4],lmlist[8])
            x1,y1=lmlist[4][1],lmlist[4][2]
            x2,y2=lmlist[8][1],lmlist[8][2]
            cx,cy=(x1+x2)//2,(y1+y2)//2

            cv2.circle(img,(x1,y1),8,(255,0,255),cv2.FILLED) #index
            cv2.circle(img,(x2,y2),8,(255,0,255),cv2.FILLED)  #thumb
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)   #line between index and thumb
            cv2.circle(img,(cx,cy),8,(255,0,255),cv2.FILLED)   #midpoint

            length=math.hypot(x2-x1,y2-y1)
        # print(length)

            if length<30:
                cv2.circle(img,(cx,cy),8,(0,255,0),cv2.FILLED)   #midpoint
            if length>200:                                  #length == volper
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        # hand range 40 - 170
        # Vol range -65 - 0
            vol=np.interp(length,[20,160],[minVol,maxVol])
            volBar=np.interp(length,[20,160],[400,100])
            volPer=np.interp(length,[20,200],[0,100])  #200=length
            print(int(length),vol)

        # Access the pc volume
        # -------------------------------------------
        # volume.SetMasterVolumeLevel(vol, None)   
        # ---------------------------------------------
    
        cv2.rectangle(img,(30,100),(85,400),(255,0,0),3)  #drawing volume bar
        cv2.rectangle(img,(30,int(volBar)),(85,400),(255,0,0),cv2.FILLED) #drawing filled bar
        cv2.putText(img,f'{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    
        

        # cv2.putText(img,f'fps:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        # cv2.imshow('img',img)
        return img
    
 
    



def main():
    ctime=0
    ptime=0
    cap=cv2.VideoCapture(0)
    wCam,hCam = 1280,720
    cap.set(3,wCam)
    cap.set(4,hCam)
    detector=handdetector()
    while True:
        success,img=cap.read()
        img=detector.Findhands(img)
        lmlist,_=detector.findPosition(img)
        if (len(lmlist))!=0:
            print(lmlist[4])
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),2)
        cv2.imshow("HandTrack",img)
        if cv2.waitKey(1) == ord('q'):
            break
    

if __name__ == "__main__":
    main()