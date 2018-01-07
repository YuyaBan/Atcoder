A,B,C,D = input().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]

L= A + B
R = C + D

if L>R:
	print("Left")
elif L==R:
	print("Balanced")
else:
	print("Right")
