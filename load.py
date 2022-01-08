import time
import sys
import random

def loading(accessname):
	def backspace(n):
		sys.stdout.write((b'\x08' * n).decode()) # use \x08 char to go back   
	l=['|','/','-','\\']
	# l=['>','>>','>>>','>>>>']
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
	