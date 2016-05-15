def Ispalindrome(num):
	length=len("%d"%num)
	if(length%2!=0):
		return False
	else:
		s=str(num)
		leng=length/2
		for i in range(leng):
			if(s[i]!=s[length-1-i]):
				return False
		
		return True

def distribute(num):
	start=100

	while start<1000:
		if(num%start==0):
			result=num/start
			if((result<1000)&(result>100)):
				print(start)
				print(result)
				print("result")
				return True
		start=start+1
	return False

i=999999
while i>100000:
	if(Ispalindrome(i)):
		if(distribute(i)):
			print(i)
			break
	i=i-1