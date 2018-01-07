#AtcoderABC003 #4
'''
nCk (mod MOD) = n! (mod MOD) * (k!)MOD-2 * ((n-k)!)MOD - 2 
'''

#以下のcom関数を用いて組み合わせを計算
def com(n, r, mod, g1, g2, inverse):
	if ( r<0 or r>n ):
		return 0
	r = min(r, n-r)
	return g1[n] * g2[r] * g2[n-r] % mod


R,C = input().split(' ')
R,C = [int(R),int(C)]

X,Y = input().split(' ')
X,Y = [int(X),int(Y)]

D,L = input().split(' ')
D,L = [int(D),int(L)]

mod = 10**9+7  #出力の制限
N = 900
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  #逆元テーブル
inverse = [0, 1]  #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
	g1.append( ( g1[-1] * i ) % mod )
	inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
	g2.append( (g2[-1] * inverse[-1]) % mod )


#Rの位置の選び方
h = R-X+1
#Rの位置の選び方
w = C-Y+1
#区画の選び方
a = h*w%mod

# D,Lの場所の総数
# (X*Y)!/D!*L!
B = X*Y

ans = com(B,D,mod,g1,g2,inverse)*a %mod
print(ans)
