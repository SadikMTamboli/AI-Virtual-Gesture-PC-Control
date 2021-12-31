import os
import mediapipe as mp
import cv2 
import time
# import p

from pyautogui import sleep
import HandTrack as ht
import pyautogui as pg


# cap=cv2.VideoCapture(0)
# wCam,hCam = 1280,720
# cap.set(3,wCam)
# cap.set(4,hCam) 
# detector=ht.handdetector(maxdetectionConfidence=0.8)

# perfect="Perfect"
# improperD="Maintain proper distance!"
# keys=[["Keyboard Access"],
#       [" Mouse Access"],
#       ["Volume Access"]
#       ]

# def Drawall(img,buttonlist):
#     for button in buttonlist:
#         x,y=button.pos
#         w,h=button.size
#         cv2.rectangle(img,button.pos,(x+w,y+h),(255, 150, 94),cv2.FILLED)
#         cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
#     return img
# class Button():
#     def __init__(self,pos,text,size=[600,85]):
#         self.pos=pos
#         self.size=size
#         self.text=text

#     # def draw(self,img):
        
# flag=0
# # myButton=Button([100,100],'Q')
# buttonlist=[]
# for i in range(len(keys)):
#     for j ,key in enumerate(keys[i]):
#         buttonlist.append(Button([100*j+330,100*i+170],key))
# while True:
#     success,img=cap.read()
#     img=detector.Findhands(img)
#     lmlist,bbox=detector.findPosition(img,draw=True)
#     img=Drawall(img,buttonlist)
#     # print(lmlist[8][0])
#     if lmlist:
#         # print("LM")
#         area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
#         # print(area)
#         if 150<area<1000:
#             # cv2.rectangle(img,(350,550),(800,650),(0, 255, 0),cv2.FILLED)
#             cv2.putText(img,f'Distance:',(50,600),cv2.FONT_HERSHEY_COMPLEX,1,(255, 255, 255),2)
#             cv2.putText(img,f'{str(perfect)}',(210,600),cv2.FONT_HERSHEY_COMPLEX,1,(0, 255, 0),2)

#             for button in buttonlist:
#                 x,y=button.pos
#                 w,h=button.size
#                 # print(lmlist[8])
#                 # print(x,x+w)
#                 if x<lmlist[8][1]<x+w and y<lmlist[8][2]<y+h:
                    
#                     cv2.rectangle(img,button.pos,(x+w,y+h),(255, 95, 8),cv2.FILLED)
#                     cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
#                     length,_,_=detector.findDistance(8,12,img,draw=False)
#                     length=((length//10)*10)
                    
#                     if length<35:
#                         print(button.text)
#                         cv2.rectangle(img,button.pos,(x+w,y+h),(0, 255, 0),cv2.FILLED)
#                         cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                            
#                         if button.text=="Keyboard Access":
#                             print("Y")
#                             flag=1
#                             # os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualKeyboard.py')
                            
#                             print("flag=",flag)
#                             # quit()
#                             # break
                            
#                         else:
#                             print("fail")
#                         cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)

#                         # cv2.rectangle(img,button.pos,(x+w,y+h),(0, 255, 0),cv2.FILLED)
#                         # cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                            
#                         # pg.press(button.text)
#                         time.sleep(0.15)
#         else:
#             cv2.putText(img,f'Distance:',(50,600),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#             cv2.putText(img,f'{str(improperD)}',(210,600),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                   
            
#     cv2.imshow("main",img)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cv2.destroyAllWindows()
# print("out")
# if flag==1:
#     print("Reqaccessed")
#     os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualKeyboard.py')
# else:
#     print("invalid")
import p
print("\n")
print("Welcome To AI Virtual Gesture PC Control".center(210,'-'),"\n")

print("Choose your option:".center(210),"\n")
print("1:Volume".center(210),"\n\n","2:Mouse".center(210),"\n\n","3:Keyboard".center(210),"\n\n","4:Terminate".center(210))
while(1):
    # print(">>".center(210))
    n=int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t>>"))

    if n==1:
        # print("\t\t\t\t\tThis will take a moment...")
        sleep(1)
        
        p.loading('Volume')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VolumeControl.py')
        
    elif n==2:
        p.loading('Mouse')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/Virtualmouse.py')
        # sleep(0.5)
    elif n==3:
        p.loading('Keyboard')
        # print("\n")
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualKeyboard.py')
        sleep(0.5)
    elif n==4:
        p.loading('Closing')
        sleep(0.3)
        break
    else:
        print("INVALID".center(210))
        sleep(0.5)

