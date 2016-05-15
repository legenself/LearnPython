


Li=[]
i=2
num=600851475143
temp=num
while temp!=1:
	print(temp)
	if(temp%i==0):
		temp=temp/i
		Li.append(i)
		i=2;
		continue
	i=i+1


print(Li)