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
				for k in range(1,m):
					if x[i+k] == y[j+k]:
						new_subs = new_subs + x[i+k]
					else:
						break
				if len(current_subs) < len(new_subs):
					current_subs = new_subs



	return len(current_subs)


LCS_TABLE = {}
def LCS(x,y,i,j):
	if (i,j) in LCS_TABLE:
		return LCS_TABLE[i,j]
	else:
		if len(x) == 0 or len(y) == 0:
			LCS_TABLE[i,j] = 0
		if i < 0 or j < 0:
			LCS_TABLE[i,j] = 0
		if x[i] == y[j]:
			LCS_TABLE[i,j] = LCS(x,y,i-1,j-1) + 1
		else:
			LCS_TABLE[i,j] = 0

	return LCS_TABLE[i,j]



def LCS_DRIVER(x,y):
	current_subs = 0
	for i in range(len(x)):
		for j in range(len(y)):
			new_subs = 	LCS(x,y,i,j)
			if current_subs < new_subs:
				current_subs = new_subs

	return current_subs



def LCS_S(x,y,i,j):
	
	if len(x) == 0 or len(y) == 0:
		return 0

	if i < 0 or j < 0:
		return 0

	s1 = s2 = s3 = s4 = 0
	if x[i] == y[j]:
		return LCS_S(x,y,i-1,j-1) + 1
		
	else:
		s2 =  LCS_S(x,y,i,j-1)
		s3 =  LCS_S(x,y,i-1,j)
		return max(s2,s3)



x = 'thecatruns'
y = 'acatran'


z = LCS_BRUTE_FORCE(x,y)
t = LCS_S(x,y,len(x)-1,len(y)-1)
q = LCS_DRIVER(x,y)
#q = LCS(x,y,6,4)

print(z,t,q)


