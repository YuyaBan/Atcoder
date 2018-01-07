#AtcoderABC003 #2
N = input()
N = str(N)
fx=0

for s in N:
	fx += int(s)

if(int(N)%fx == 0): print('Yes')
else: print('No')
