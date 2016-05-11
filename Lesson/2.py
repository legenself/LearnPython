print(abs(-100))

def my_abs(x):
	if (not isinstance(x,(int,float))):
		return TypeError("bad operand type")
	elif(x>=0):
		return x
	else:
		return -x
print (my_abs("A"))

def nop():
	pass

import math

def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

print(move(100,100,60,math.pi/6))

def power(x,n=2):
	s=1
	while n>0:
		s=x*s
		n=n-1
		
	return s

print(power(5))

def add_end(L=None):
	if L is None:
		L=[]
	L.append("end")
	return L
print(add_end())