# Author Lutfar Rahman


def LCS_BRUTE_FORCE(x,y):
	
	if len(x) == 0 or len(y) == 0:
		return ''
	if len(x) == 1 and len(y) == 1:
		if x[0] == y[0]:
			return x[0:]
		else:
			return ''

	current_subs = ''
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i] == y[j]:
				m = min(len(x)-i,len(y)-j)
				new_subs = x[i]
				for k in range(1,m-1):
					if x[i+k] == y[j+k]:
						new_subs = new_subs + x[i+k]
					else:
						break
				if len(current_subs) < len(new_subs):
					current_subs = new_subs



	return current_subs



x = 'thecatruns'
y = 'acatran'


z = LCS_BRUTE_FORCE(x,y)
print(z)


