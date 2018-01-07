N = int(input())
w = []
sum = N

for i in range(N):
    w.append(input())
  
for x in range(N):
	for y in range(x+1,N):
		if w[x] == w[y]:
			w[x] = 0
    		sum -= 1

print(abs(sum))