#AtcoderABC081 #3
'''
10 3
5 1 3 2 4 1 1 2 3 4
3
'''
'''
N,K = input().split(' ')
N,K = [int(N),int(K)]
#A = list(map(int, input().split(' ')))
A=list(int(_) for _ in input().split()) 

list=[]
cnt = 0
ans = 0

for n in range(N+1):
	if (A.count(n)) > 0:
		cnt += 1
		list.append(A.count(n))

list.sort()

if cnt > K:
	for n in range(cnt-K): ans += list[n] 

print(ans)
'''
from collections import Counter

N, K = list(map(int,input().split()))
listA = Counter(input().split())

print(listA)
listA = list(listA.values())
print(listA)

listA.sort()
times = len(listA) - K

num = 0

if times <= 0:
    num = 0
else:
    for i in range(times):
        num += listA[i]

print(num)