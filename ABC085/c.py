'''
x+y+z=N
10000x+5000y+1000z=Y

z=N-x-y
10000x+5000y+1000(N-x-y)=Y
=> 9000x+4000y=Y-1000N
=> 9x+4y=(Y/1000)-N

'''
A = list(map(int, input().split(' ')))
N = A[0]
Y = A[1]
ans =[]
#print('N:{},Y:{}'.format(N,Y))

right = (Y/1000) - N
#print('right:{}'.format(right))


for x in range(N+1):
	for y in range(N-x+1):
		tmp = 9*x + 4*y
		#print('x:{},y{},tmp:{}'.format(x,y,tmp))
		if tmp == right and x+y <= N:
			print('{} {} {}'.format(x,y,(N-x-y)))
			quit()

print('-1 -1 -1')