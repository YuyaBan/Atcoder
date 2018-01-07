#AtcoderABC003 #3

def calc(F,P,w,N):
	tmp = 0
	for j in range(N):
		cnt = 0
		for i in range(10):
			if w[i] == F[j][i] and w[i] == 1: cnt += 1
		tmp += P[j][cnt]
	return tmp


w = [0,0,0,0,0,0,0,0,0,0] 
sam = [0,0,0,0,0,0,0,0,0,0]
N = int(input())
ans = -10000
earn = 0
flag = 0
cnt = 0


F=[]
for i in range(N):
	tmp = list(map(int, input().strip().split(' ')))
	F.append(tmp)

P=[]
for i in range(N):
	tmp = list(map(int, input().strip().split(' ')))
	P.append(tmp)

ans2 =[]
for i0 in range(2):
	for i1 in range(2):
		for i2 in range(2):
			for i3 in range(2):
				for i4 in range(2):
					for i5 in range(2):
						for i6 in range(2):
							for i7 in range(2):
								for i8 in range(2):
									for i9 in range(2):
										w = [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9]
										if flag = 0: flag = 1
										else: earn = calc(F,P,w,N)
										if earn > ans:
											ans = earn
											ans2 = w
										if w == sam:
											print('debug')
											print(w)
											print(flag)
											print(cnt)
										cnt +=1

print(ans)
print(ans2)