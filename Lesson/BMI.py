height=1.75
weight=80.5

bmi=weight/(height*height)

if bmi<18.5:
	print("too light")
elif (bmi<25) & (bmi>18.5):
	print("normal")
elif (bmi>25):
	print("weight")
