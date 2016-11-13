# Author Lutfar Rahman
import time
import util

def LCS_BRUTE_FORCE(x,y):
	'''
	Calculates the length of the longest common substring of x and y[:j+1]
	with the brute force style
	'''
	
	if len(x) == 0 or len(y) == 0:
		return 0

	current_subs = 0
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i] == y[j]:
				m = min(len(x)-i,len(y)-j)
				new_subs = 1
				for k in range(1,m):
					if x[i+k] == y[j+k]:
						new_subs += 1
					else:
						break
				current_subs = max(current_subs,new_subs)

	return current_subs


LCS_TABLE = {}
def LCS(x,y,i,j):
	
	'''
	Calculates the length of the longest common substring of x[:i+1] and y[:j+1]
	when x[i] and x[j] is must to include
	'''
	if (i,j) not in LCS_TABLE:
		if i < 0 or j < 0 :
			LCS_TABLE[i,j] = 0
		elif x[i] == y[j]:
			LCS_TABLE[i,j] = LCS(x,y,i-1,j-1) + 1
		else:
			LCS_TABLE[i,j] = 0

	return LCS_TABLE[i,j]



def LCS_DRIVER(x,y):

	'''
	Calculates the length of the longest common substring of x and y
	with Dynamic Programming
	'''

	max_lcs = 0
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			if x[i] == y[j]:  #optimization from the driver program
				lcs_new = LCS(x,y,i,j)
				max_lcs = max(max_lcs,lcs_new)

	return max_lcs



# x = 'thecatruns'
# y = 'acatran'
# z = LCS_BRUTE_FORCE(x,y)
# q = LCS_DRIVER(x,y)
# print(z,q)




for n in range(10,3000,300):

	x = util.random_str(n)
	y = util.random_str(n)

	start = time.time()
	ans = LCS_BRUTE_FORCE(x,y)
	end = time.time()
	print("brute force:",end-start,ans)

	start = time.time()
	LCS_TABLE = {}
	ans = LCS_DRIVER(x,y)
	end = time.time()
	print("DP:",end-start,ans)

	print('')


