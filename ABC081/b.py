#AtcoderABC081 #2

def div(A,N):
	for n in range(N):
		A[n] = A[n]//2

N = int(input())
A = list(map(int, input().split(' ')))
f = 1
cnt = 0
ans = 0

while True:
	for a in A:
		if(a%2 == 0): cnt += 1
	if cnt == N: 
		div(A,N)
		ans += 1
		cnt = 0
	else: break

print(ans)