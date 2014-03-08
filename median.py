
from math import floor, ceil, sqrt
from random import randint
from time import time

def median(S):
	''' Size of S must be large or else you get index out of bounds issues
	'''
	n = len(S)

	R_size = int(ceil(n ** (.75)))
	R_ind = [randint(0,n-1) for i in range(R_size)]

	R = [S[i] for i in R_ind]

	R_sorted = sorted(R)

	down_ind = max(int(floor((n ** (.75))/2.0 - sqrt(n))),0)
	up_ind = min(int(floor((n ** (.75))/2.0 + sqrt(n))), len(R_sorted)-1)

	#print down_ind, up_ind, len(R_sorted)
	down, up = R_sorted[down_ind], R_sorted[up_ind]

	C = [s for s in S if s>=down and s<= up]
	l = len([s for s in S if s<down])
	r = len([s for s in S if s>up])

	if l>n/2 or r>n/2:
		return False

	if len(C)> 4 * n**.75:
		return False

	C_sorted = sorted(C)

	#print n/2 + 1 - l, l, r, len(C)
	median = C_sorted[ min(n/2 + 1 - l, len(C_sorted)-1)]

	return median

def main():
	
	num_exp = 10000
	max_element = 1000000
	max_size = 10000

	num_fails = 0

	num_bad_median = 0

	for i in range(num_exp):
		size = randint(3,max_size-1)

		S = [randint(0,max_element) for j in range(size)]

		#start = time()
		middle = median(S)
		#elapsed = time()-start
		#print elapsed

		if middle==False:
			num_fails += 1
			continue

		#start = time()
		S_sorted = sorted(S)
		middle_control = S_sorted[len(S_sorted)/2 + 1]
		#elapsed = time()-start
		#print elapsed

		if middle_control!=middle:
			num_bad_median += 1

		#print middle, middle_control

	print float(num_fails) / float(num_exp)
	print "\n"

	print num_bad_median

if __name__=="__main__":
	main()