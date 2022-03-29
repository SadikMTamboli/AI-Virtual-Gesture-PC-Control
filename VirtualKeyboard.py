import mediapipe as mp
import cv2 
import time
import HandTrack as ht
import pyautogui as pg
import numpy as np

cap=cv2.VideoCapture(0)
wCam,hCam = 1280,720
cap.set(3,wCam)
cap.set(4,hCam) 
logo = cv2.imread('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
siz = 50

logo = cv2.resize(logo,(siz,siz))

# # Create a mask of logo
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
# print(mask)
finaltext=""
detector=ht.handdetector(maxdetectionConfidence=0.8)
perfect="Perfect"
improperD="Maintain proper distance!"

keys=[["1","2","3","4","5","6","7","8","9","0","<-"],
      ["Q","W","E","R","T","Y","U","I","O","P","=>"],
      ["A","S","D","F","G","H","J","K","L",";",":"],
      ["Z","X","C","V","B","N","M",",",".","/","@"],
      ["wi","Sp","<",">","^","v","nt"]]


def Drawall(img,buttonlist):
    for button in buttonlist:
        x,y=button.pos
        w,h=button.size
        cv2.rectangle(img,button.pos,(x+w,y+h),(255, 150, 94),cv2.FILLED)
        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    return img

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos=pos
        self.size=size
        self.text=text

    # def draw(self,img):
        
        
# myButton=Button([100,100],'Q')

buttonlist=[]
for i in range(len(keys)):
    for j ,key in enumerate(keys[i]):
        buttonlist.append(Button([100*j+50,100*i+50],key))
flg=0
while True:
    success,img=cap.read()
    frame=img
    roi = frame[-siz-130:-130, -siz-1175:-1175]
    
	# Set an index of where the mask is
    roi[np.where(mask)] = 0
    roi += logo

    img=detector.Findhands(img)
    lmlist,bbox=detector.findPosition(img,draw=True)
    img=Drawall(img,buttonlist)
    # print(lmlist[8][0])
    if lmlist:
        # print("LM")
        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        # print(area)
        if 150<area<1000:
            # cv2.rectangle(img,(350,550),(800,650),(0, 255, 0),cv2.FILLED)
            cv2.putText(img,f'Distance:',(100,620),cv2.FONT_HERSHEY_COMPLEX,1,(255, 255, 255),2)
            cv2.putText(img,f'{str(perfect)}',(270,620),cv2.FONT_HERSHEY_COMPLEX,1,(0, 255, 0),2)
            
            for button in buttonlist:
                x,y=button.pos
                w,h=button.size
                # print(lmlist[8])
                # print(x,x+w)
                if x<lmlist[8][1]<x+w and y<lmlist[8][2]<y+h:
                    
                    cv2.rectangle(img,button.pos,(x+w,y+h),(255, 95, 8),cv2.FILLED)
                    cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                    length,_,_=detector.findDistance(8,12,img,draw=False)
                    length=((length//10)*10)
                    
                    if length<35:
                        print(button.text)

                        if button.text=='=>':
                            pg.press('enter')
                            print("Entr")

                        elif button.text=='wi':
                            pg.press('win')
                            print("win")
                        
                        elif button.text=="Sp":
                            pg.press("space")
                            print("space")
                            
                        elif button.text=="<":
                            pg.press("left")
                            print("left")
                        
                        elif button.text==">":
                            pg.press("right")
                            print("right")
                        
                        elif button.text=="^":
                            pg.press("up")
                            print("up")
                        
                        elif button.text=="v":
                            pg.press("down")
                            print("dn")
                        
                        elif button.text=='<-':
                            pg.press('backspace')
                            print("BS")
                        
                        elif button.text=='nt':
                            if flg==0:
                                pg.press('win')
                                pg.typewrite('notepad')
                                pg.press('enter')
                                flg=1
                            
                        else:
                            
                            cv2.rectangle(img,button.pos,(x+w,y+h),(0, 255, 0),cv2.FILLED)
                            cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                            finaltext+=button.text
                            pg.press(button.text)
                            time.sleep(0.15)
                        

        else:
            cv2.putText(img,f'Distance:',(100,620),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,f'{str(improperD)}',(270,620),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    
    cv2.rectangle(img,(50,640),(1190,710),(255, 150, 94),cv2.FILLED)
    cv2.putText(img,finaltext,(60,700),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    

    
    

    # backspace
    # cv2.rectangle(img,(100,450),(300,450),(255, 150, 94),cv2.FILLED)
    # cv2.putText(img,f'<-',(110,450),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)


    # img=myButton.draw(img)
    cv2.imshow("VirtualKeyboard",img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()