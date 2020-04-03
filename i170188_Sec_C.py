######################   KMP
def prefix(st):
	length=len(st)
	pre=[0]*length
	i=1
	while(i<length):
		j=pre[i-1]
		while (j > 0 and st[i] != st[j]):
			j=pre[j-1]
		if (st[i] == st[j]):
			j=j+1
		pre[i]=j
		i=i+1
	return pre
print(prefix("aabaa"))
###################  Q2_Robin Karp
def Robin(text,pat,q):
	l_t=len(text)
	l_p=int(pat)
	print(l_t)
	i=0
	test=l_p % l_t
	sh=0
	while(i<l_t-1):
		t=int(text[i])
		t=t+(int(text[i+1]*10))
		if(t%q==test):
			sh=sh+1
		i=i+1
	return test
print(Robin("31415926535","26",11))
