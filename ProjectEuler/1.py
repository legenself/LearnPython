n=1000

L=range(n)

S=set(L[0:n:3])|set(L[0:n:5])

print(sum(S))
