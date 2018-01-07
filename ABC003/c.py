#AtcoderABC003 #3

N,K = input().split(' ')
N,K = [int(N),int(K)]

R = list(map(int, input().strip().split(' ')))
R.sort(reverse=True)
rate = 0.0

for n in reversed(range(K)):
	rate = (rate + R[n])/2.0

print("{:.6f}".format(rate))