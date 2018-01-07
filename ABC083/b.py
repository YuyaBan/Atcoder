N,A,B=input().split(' ')
N,A,B = [int(N),int(A),int(B)]
SUM = 0

for i in range(N+1):
	I = str(i)
	array = list(map(int, list(I)))
	s = sum(array)
	#print(s)
	if A <= s and s <= B:
		#print(i)
		SUM += i
print(SUM)