n = raw_input()

l = [int(x) for x in list(str(n))]
if l[0] == 9:
	print("Yes")
elif l[1] == 9:
	print("Yes")
else:
	print("No")
