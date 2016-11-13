

Table = {}
def LCS_S(x,y,i,j):
	'''
	Calculates the length of the longest common subsequence of x[:i+1] and y[:j+1]
	'''
	
	if (i,j) not in Table:
		if i < 0 or j < 0 :
			Table[i,j] = 0

		elif x[i] == y[j]:
			Table[i,j] = LCS_S(x,y,i-1,j-1) + 1
				
		else:
			s1 =  LCS_S(x,y,i,j-1)
			s2 =  LCS_S(x,y,i-1,j)
			Table[i,j] = max(s1,s2)

	return Table[i,j]




x = 'thecatruns'
y = 'acatran'
t = LCS_S(x,y,len(x)-1,len(y)-1)
print(t)

import util
for i in range(10):
	Table = {}
	x = util.random_str(100)
	y = util.random_str(100)
	t = LCS_S(x,y,len(x)-1,len(y)-1)
	print("length:",t)


