a=1
b=2
ve=[a,b];
i=2
while a:
	temp=ve[i-1]+ve[i-2]
	if(temp>4000000):
		break
	ve.append(temp)
	i=i+1;

sum=0
for x in ve[:]:
	sum=sum+x
print(ve)
print(sum)
