A = list(map(int, input().split(' ')))
S = input()

if S[0:A[0]].isdigit() == False or S[A[0]+1:].isdigit() == False or S[A[0]] != '-' or len(S[0:A[0]]) != A[0] or len(S[A[0]+1:]) != A[1] :
	print('No')
else:
	print('Yes')