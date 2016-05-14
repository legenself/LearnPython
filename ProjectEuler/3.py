# num=600851475143

Li=[]
def isfactor(num):
    i=2
    r=True
    if(num  in Li):
    	return r
    while i<num:
    	print(str(num)+" now is " + str(i))
    	if(num%i==0):
    		r=False
    		break
    	i=i+1
    if(r):
    	Li.append(i)
    return r


def distribute(num):
	x=num-1
	while num%x!=0:
		d=num/x
		if(x  not in Li)&(isfactor(x)==False):
			distribute(x)
		
		if(d  not in Li)&(isfactor(d)==False):
			distribute(x)
		x=x-1
# print(isfactor(4))

num=24
distribute(num)
print(Li)
# x=2
# while 1:
# 	x=x-1
# 	print(str(x))
# 	if(isfactor(x))
# 	if(num%x==0)&(isfactor(x)):
# 		print("Answer is"+str(x))
# 		break

