print('hello')
print('hello','world','everyone')

print(100)

print(100+300)

print('100+300=',100+300)

#name =input('input your name')

#print("hello",name)

a=100
if a>0:
    print(a)
else:
    print(-a)

#there are some notice
print('''line1
	...line2
	...line3''')
classmates=['Michael',"Bob","Trace"]
print(classmates)

print(len(classmates))

print(classmates[0])

print(classmates[-1])

classmates.append('adam')

print(classmates)

print(classmates.pop())

print(classmates.pop(1))

classmates[1]="legen"

print(classmates)

L=["123",123,True]

print(L)

s=['python','java',['asp','php'],'scheme']

print(len(s))

classmates=('Michael','Bob','Tracy')

print(classmates)

# tuple (1) => (1,)
L=[
	['Apple','Google','MicroSoft'],
	['Java','Python','php'],
	['adam','Bart','Lisa']
]
print(L[0][0])

print(L[1][1])

print(L[2][2])

for name in L:
	print(name)
sum=0
for x in range(101):
	sum+=x
print(sum)

s1=set([1,2,34,3,56])
s2=set([34,3,57,3,3,6,8])

print(s1&s2)
print(s1|s2)