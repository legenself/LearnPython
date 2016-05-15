
Li={}
def AddIfNotEnough(Ls):
	for key in Ls.keys():
		val=Li.get(key)
		if(val!=None):
			if(val<Ls.get(key)):
				Li[key]=Ls.get(key)
		else:
			Li[key]=Ls.get(key)
	print(Li)

for x in range(21)[1:]:
	Ls={}
	i=2
	temp=x
	while temp>1:
		if(temp%i==0):
			if(Ls.has_key(i)):
				Ls[i]=Ls[i]+1
			else:
				Ls[i]=1
			temp=temp/i
			i=2
			continue
		i=i+1

	if(len(Ls)==0):
		Ls[x]=1
	AddIfNotEnough(Ls)
print("over")

result=1
for x in Li:
	print(x)
	print(Li[x])
	result=result* (x**Li[x])

print(result)

