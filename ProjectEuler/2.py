
sum=2
a=1
b=2
temp=0
while temp<4000000:
	temp=a+b
	if temp%2==0:
		sum+=temp
	a=b
	b=temp


print(sum)

