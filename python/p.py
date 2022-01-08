# import streamlit as st
# st.success("hello")





# cp  = st.number_input("CP:",step=1, min_value=0, max_value=3,value=1)

# def GCD(a,b):
#     if b==0:
#         return a
#     else:
#         return GCD(b,a%b)
# c=GCD(75,100)
# # print(c)
# n=370
# s=0
# t=n
# while(t>0):
#    d=t%10
#    s+=d**3   
#    t=t//10
# if n==s:
#    print("A")
# else:
#    print("NA")
# n=list(map(int,input(">>").split()))
# print(n)
# l=[]
# c=0
# for i in range(len(n)):
#     if i!=(len(n)-1):
#         l.append(n[i]*n[i+1])
# s,i,=0,0
# c=0
# print(l)
# for i in range(len(l)):
#     if i!=(len(l)+1):
#         s=s+l[i]
    
# print(s)

# n=input(">>")
# print("",eval(n))
# low=int(input())
# up=int(input())
# for i in range(low,up+1):
#     if(up>=100):
#          print("{:03d}".format(i),end=" ")
#     elif(up>=10):
#         print("{:02d}".format(i),end=" ")
#     else:
#         print(i,end=" ")
# n=str(input(">>"))
# print(int(n,2))
# for i in range(5):
#     print("\U0001F602")


# --------------------------perfect math------------------------
# n=int(input("n:"))
# m=int(input("m:"))
# l=[]
# for i in range(n):
#     l.append(int(input()))
# print(l)
# s=0
# for i in range(len(l)):
#     # print(i)
#     s+=(l[i]%m)
# print(s)
#-------------------------------removing duplicate no
# n=list(map(int,input(">>").split()))
# l=[]
# for i in range(len(n)):
#    if n[i] not in l:
#        l.append(n[i]) 
# print(l)
# n=list(map(int,input(">>").split()))
# pair=0
# sets=set(n)
# for i in sets:
#     count=n.count(i)
#     pair+=count//2
# print(pair)
# # for i in range(len(n)):
# l=[[0,2,5,2],[5,6,9,2],[5,6,2]]
# l1=[[0,2,5,2],[5,6,9,2],[5,6,2]]
# if l[0]==l1[0]:
#     print("Y")
# else:
#     print("N")
# print(l[0],l1[0])

# l=1,1,1,2
# print(list(l))
# if 1599>1200:
#     print("y")
# else:
#     print("no")
# import speech_recognition as sr
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     print("Say something.... ")
#     audio=r.listen(source)
#     try:
#         print("You Said:\n"+r.recognize_google(audio))
#     except Exception as e:
#         print("Error:"+str(e))

# from time import sleep, time
# import pyautogui
# print(pyautogui.position())
# # pyautogui.press('win')
# pyautogui.hotkey('win','down')
# pyautogui.typewrite(['importpyautogui','enter',"pyautogui.hotkey('win',2)"], interval=0.15)
# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.15)
# # pyautogui.press('backspace')
# # pyautogui.press("win")
# pyautogui.hotkey('win','2')
# for i in range(100):
#     pyautogui.scroll(-1000)#     sleep(1)



# Python3 implementation of the approach

# Pattern table from Case 1
# values = {
# 	1: 0,
# 	10: 4,
# 	100: 4,
# 	1000: 454,
# 	10000: 454,
# 	100000: 45454,
# 	1000000: 45454,
# 	10000000: 4545454,
# 	100000000: 4545454,
# 	1000000000: 454545454,
# 	10000000000: 454545454,
# 	100000000000: 45454545454,
# 	1000000000000: 45454545454,
# 	10000000000000: 4545454545454,
# 	100000000000000: 4545454545454,
# 	1000000000000000: 454545454545454,
# 	10000000000000000: 454545454545454,
# 	100000000000000000: 45454545454545454,
# 	1000000000000000000: 45454545454545454,
# }

# # Function that returns the number of
# # even and odd digits in val
# def count_even_odd(val):
# 	even = odd = 0
# 	while val > 0:
# 		num = val % 10
# 		if num % 2 == 0:
# 			even += 1
# 		else:
# 			odd += 1
# 		val //= 10

# 	return even, odd

# # Function that returns True if num
# # satisfies the given condition
# def satisfies_condition(num):
# 	even, odd = count_even_odd(num)
# 	if even % 2 == 1 and odd % 2 == 0:
# 		return True
# 	return False


# # Function to return the count of numbers
# # from 1 to val that satisfies the given condition
# def count_upto(val):

# 	# If the value is already present in the
# 	# values dict
# 	if int(val) in values:
# 		return values[int(val)]

# 	# If the value is even
# 	# Case 2
# 	if len(val) % 2 == 0:
# 		return values[int('1' + '0' * (len(val) - 1))]

# 	val_len = len(val)
# 	count = values[int('1' + '0' * (val_len - 1))]

# 	# Now the problem is to count the desired
# 	# numbers from 10**(val_len-1) + 1 to val
# 	left_end = int('1' + '0' * (val_len - 1)) + 1

# 	# Case 3
# 	# Eliminating all the even numbers
# 	count += (int(val) - left_end) // 2

# 	if satisfies_condition(int(val)) or satisfies_condition(left_end):
# 		count += 1
# 	return count

# def cpm(p,L,R):

# if __name__ == '__main__':

# 	# Input L and R ( as a string )
# 	l, r = '5', '25'

# 	right = count_upto(r)

# 	left = 0
# 	if(l == '1'):
# 		left = 0
# 	else:
# 		left = count_upto(str(int(l)-1))

# 	print(right - left)
    
#     cpm(p,l,r)
# def s(a):
#     alpha = ""
#     num = ""
#     special = ""
#     for i in range(len(a)):
#         if (str[i].isdigit()):
#             num = num+ a[i]
#         elif((str[i] >= 'A' and a[i] <= 'Z') or
#              (str[i] >= 'a' and a[i] <= 'z')):
#             alpha += a[i]
#         else:
#             special += a[i]
#     print(alpha)
#     print(num )
#     print(special)
# a=input()
# s(a)    
# importing Image class from PIL package

# importing the libraries
# import cv2
# import numpy as np

# # Setup camera
# cap = cv2.VideoCapture(0)

# # Read logo and resize
# logo = cv2.imread('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
# siz = 50

# logo = cv2.resize(logo,(siz,siz))

# # # Create a mask of logo
# img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

# while True:
# 	# Capture frame-by-frame
# 	ret, frame = cap.read()

# 	# Region of Image (ROI), where we want to insert logo
# 	roi = frame[-siz-100:-100, -siz-100:-100]

# 	# Set an index of where the mask is
# 	roi[np.where(mask)] = 0
# 	roi += logo

# 	cv2.imshow('WebCam', frame)
# 	if cv2.waitKey(1) == ord('q'):
# 		break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()




# class account:
# 	def __init__(self,accno,name,balance) -> None:
# 		self.accno=accno
# 		self.name=name
# 		self.balance=balance
# 	def deposite_money(self,dmoney):
# 		self.balance=self.balance+ dmoney
# 		return self.balance
# 	def withdraw_m(self,with_draw):
# 		if self.balance -with_draw>=1000:
# 			self.balance-=with_draw
# 			return self.balance		
# 		else:
# 			return 0

# accno=int(input("accno:"))
# name=input("Name:")
# balance=int(input("bal:"))
# accout=account(accno,name,balance)
# n=input("D / W :")
# if n=='D':
# 	d=int(input("amount:"))
	
# 	print("deposited:",accout.deposite_money(d))
# elif n=='W':
# 	w=int(input("Wamount"))
# 	rw=accout.withdraw_m(w)
# 	if rw==0:
# 		print("insufficient balance")
# 	else:
# 		print("balance:",rw)

# class Employee:
# 	def __init__(self,empid,empname,emprole,empsalary) -> None:
# 		self.empid=empid
# 		self.empname=empname
# 		self.emprole=emprole
# 		self.empsalary=empsalary

# 	def increasesal(self,percentage):
# 		self.empsalary+=self.empsalary*percentage*0.01
# 		return self.empsalary

# class organition:
# 	def __init__(self,orgname,emplist) -> None:
# 		self.orgname=orgname
# 		self.emplist=emplist
	
# 	def calculateincre(self,erole,increper):
# 		emp=[]
# 		for i in self.emplist:
# 			if i.emprole==erole:
# 				i.empsalary+=i.empsalary*increper*0.01
# 				emp.append(i)
# 		return emp

# n=int(input(">>"))
# emplist=[]
# for i in range(n):
# 	print(i+1)
# 	empid=int(input("eid:"))
# 	ename=input("ename:")
# 	erole=input("erole")
# 	esal=int(input("esal:"))
# 	emplist.append(Employee(empid,ename,erole,esal))
# # print(emplist)
# o=organition('abc',emplist)
# role=input("erole:")
# per=int(input("percent:"))
# r=o.calculateincre(role,per)
# if len(r)!=0:
# 	for i in r:
# 		print(i.empname,i.empsalary)
# else:
# 	print("no emp found")




# class Account:
# 	def __init__(self,accno,accname,accbal):
# 		self.accno=accno
# 		self.accname=accname
# 		self.accbal=accbal
	
# 	def depositeamt(self,amt):
# 		self.accbal+=amt
# 		return self.accbal
	
# 	def withamt(self,amt):
# 		if self.accbal-amt>=1000:
# 			self.accbal-=amt
# 			return 1
# 		else:
# 			return 0

# accno=int(input("Acno:"))
# accname=input("acname")
# accbal=int(input("acbal:"))
# a=Account(accno,accname,accbal)
# dep=int(input("D:"))
# withd=int(input("W:"))
# r=a.depositeamt(dep)
# w=a.withamt(withd)
# print(r)
# if w==1:
# 	print(a.accbal)
# else:
# 	print("insuf_bal")

# class Employee:
# 	def __init__(self,empno,empname,leaves) -> None:
# 		self.empno=empno
# 		self.empname=empname
# 		self.leaves=leaves

# class company:
# 	def __init__(self,cname,emplist=[]) -> None:
# 		self.cname=cname
# 		self.emplist=emplist
	
# 	def displeave(self,empno,leavetype):
# 		for i in self.emplist:
# 			if i.empno==empno:
# 				return i.leaves(leavetype)
	
# 	def leavappln(self,empno,etype,n_of_leav):
# 		for i in self.emplist:  
# 			if i.empno==empno:
# 				if n_of_leav>=i.leaves[etype]:
# 					print('granted')
# 				else:
# 					print('rejected')
# n=int(input(">>"))
# leaves={}
# emp=[]
# c=company('abc')
# for i in range(n):
# 	print(i+1)
# 	empno=int(input("empno:"))
# 	ename=input("Ename:")
# 	leaves['EL']=int(input("EL:"))
# 	leaves['CL']=int(input("CL:"))
# 	leaves['SL']=int(input("SL:"))
# 	e=Employee(empno,ename,leaves)
# 	c.emplist.append(e)
	
# eno=int(input("eno:"))
# lt=input("lt:")
# nol=int(input("nol:"))

# print(c.displeave(eno,lt))
# print(c.leavappln(eno,lt,nol))
# import cv2
# c=100
# l=['|','/','-','\ ']
# i=0
# lp=len(l)

# while(c>=0):
# 	if i<=lp:
# 		p=l[i]
# 		print(p,end=" ")
# 		i+=1
# 		if i==len(l):
# 			i=0
	
# 	c-=1
# import time   

# def backline():        
#     print('\r', end='')                     # use '\r' to go back


# for i in range(101):                        # for 0 to 100
#     s = str(i) + '%'                        # string for output
#     print(s, end='')                        # just print and flush
#     backline()                              # back to the beginning of line    
#     time.sleep(0.2)                         # sleep for 200ms


import time
import sys
import random

def loading(accessname):
	def backspace(n):
		sys.stdout.write((b'\x08' * n).decode()) # use \x08 char to go back   
	l=['|','/','-','\\']
	i=0
	
	lp=len(l)
	if accessname=='Closing':
		c= random.randint(1,8)
		
		print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t{accessname}...",end="")
	else:
		c= random.randint(15,25)
		
		print(f"\n\t\t\t\t\t\t\t\t\t\t\t\tGetting things for {accessname}...",end="")
	while(c>=0):
		if i<=lp:
			s = l[i]								# string for output
		                        
			sys.stdout.write(s)                     # just print
			i+=1
			sys.stdout.flush()                      # needed for flush when using \x08
			backspace(len(s))                       # back n chars    
			time.sleep(0.1)                         # sleep for 200ms
			if i==len(l):
				i=0                        # for 0 to 100
	
		c-=1
	return ""
# loading('Closng')
	