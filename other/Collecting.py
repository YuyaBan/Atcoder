#Collecting.py
import math
N,K=input(),input()
x = [int(_) for _ in raw_input().split()]
sum = 0

for i in range(N):
	if K < x[i]:
		sum += (x[i]-K)*2
	elif K/2 < x[i]:
		sum += (K-x[i])*2
	else:
		sum += x[i]*2
print(sum)