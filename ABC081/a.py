#AtcoderABC081 #1

s = str(input())
cnt = 0

for a in range(3):
	if s[a] == '1': cnt +=1

print(cnt)