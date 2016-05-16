def Isprime(num):
	i=2
	while i<num:
		if(num%i==0):
			return False
		i=i+1
	return True

i=2
count=0
while count<10001:
	if(Isprime(i)):
		count=count+1
		print(str(count)+" "+str(i))
		
	i=i+1


print(i-1)
