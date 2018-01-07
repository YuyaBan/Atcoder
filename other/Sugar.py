#Sugar.py
#1 2 10 20 15 200
a, b, c, d, e, f = (int(_) for _ in raw_input().split()) 

salt = []
water = []

#salt
#print('salt')
di = f/d
ci=0
while di >= 0:
	if (c*ci+d*di) <= f:
		tmp = c*ci+d*di
		salt.append(tmp)
		#print(tmp)
		#print('salt:{0} ci:{1} di:{2}'.format(tmp,ci,di))

		if (c*(ci+1)+d*di) <= f:
			ci += 1
		else:
			di -= 1
			ci = 0
	else:
		di -= 1
		ci = 0
#print(salt)

#print('water')
bi = f/(100*b)
ai=0
while bi >= 0:
	if (100*a*ai+100*b*bi) <= f:
		tmp = 100*a*ai+100*b*bi
		water.append(tmp)

		if (100*a*(ai+1)+100*b*bi) <= f:
			ai += 1
		else:
			bi -= 1
			ai = 0
	else:
		bi -= 1
		ai = 0
#print(water)

salt_ans = 0
water_ans = 0 
ans_conc = 0
dist = 0

for w in water:
#	print(i)
	for s in salt:
		if s+w == 0:
			dist = 1 + e
			#print('water:{0} salt:{1}'.format(w,s))
			#print(dist)
		elif s+w >= f:
			dist = 1 + e
		elif w == 0 :
			dist = 1 + e
		#elif s > w:
		#	dist = 1 + e
		else:
			#dist = (100*s/(s+w))
			dist = (float(100 * s)/ w)

		if dist == e:
				salt_ans = s
				water_ans = w+s
				break
		
		if dist <= e:
			conc_tmp = float(100*s)/(s+w)
			if ans_conc < conc_tmp:
				#print('s:{0} w:{1} dist:{2} e:{3}'.format(s,w,dist,e))
				#print('conc_tmp:{0}'.format(conc_tmp))
				#print('registttttttttttttttttttttttt')
				salt_ans = s
				water_ans = w+s
				ans_conc = conc_tmp
				#print('water:{0} salt:{1}'.format(water_ans,salt_ans))

print('{0} {1}'.format(water_ans,salt_ans))


