N,H = map(int,input().split())
a=[]
b=[]
for i in range(N):
	ai,bi = map(int,input().split())
	a.append(ai)
	b.append(bi)

a.sort(reverse=True)  #[4,3,2,1]
b.sort(reverse=True)  #[3,4,5,6]

lenb=len(b)

for i in range(lenb):
	if a[0] > b[-1]:
		del b[-1]
	else:
		break
cut = 0

for x in b:
	H -= x
	cut +=1
	if(H<=0):
		print(cut)
		quit()

ans = int(H%a[0])
#print('{}%{}={}'.format(H,a[0],ans))

if ans == 0: ans = H/a[0]+cut
else: ans =(H/a[0])+1+cut

print(int(ans))