#AtcoderABC003 #2
S = str(input())
T = str(input())

for n in range(len(S)):
	if (S[n] != T[n]) and (S[n] == '@') and (not 'atcoder@'.count(T[n])):
		print('You will lose')
		quit()
	elif (S[n] != T[n]) and (T[n] == '@') and (not 'atcoder@'.count(S[n])):
		print('You will lose')
		quit()
	elif (S[n] != T[n]) and (T[n] != '@') and (S[n] != '@'):
		print('You will lose')
		quit()

print('You can win')
