# Atcoder ABC003 ＃1

N=int(input())
sum =0

for a in range(N+1):
	sum += int(a * 10000)
	
sum = int(sum/(N))
print(sum)