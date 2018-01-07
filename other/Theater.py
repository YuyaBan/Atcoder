N = int(input())
sum = 0

for num in range(N):
	a, b = (int(_) for _ in raw_input().split()) 
	sum += b - a + 1

print(sum)