import math
import sys
complexity = ["on", "onlogn", "on^(3/2)", "on^2", "on^2logn", "on^3", "on^4","o2^n", "on!"]

def TLE(n, x, comp):
	if comp == 0:
		if x > n: return True
		return False
	elif comp == 1:
		if x*math.log2(x) > n: return True
		return False
	elif comp == 2:
		if x**(3/2) > n: return True
		return False
	elif comp == 3:
		if x**2 > n: return True
		return False
	elif comp == 4:
		if (x**2) * math.log2(x) > n: return True
		return False
	elif comp == 5:
		if x**3 > n: return True
		return False
	elif comp == 6:
		if x**4 > n: return True
		return False
	elif comp == 7:
		if x > math.log2(n): return True
		return False
	elif comp == 8:
		act = 1
		for i in range(int(x), 0, -1):
			act *= i
			if act > n: return True
		if act > n: return True
		return False		
		
s = []
try:
	while True:
		g = input().split()
		if len(g) != 0:
			for x in g: s.append(x)
except:
	pass

index = 0

for q in range(int(len(s)/3)):
	n = int(s[index])
	index += 1
	m = int(s[index])
	index += 1
	com = s[index]
	index += 1
	for i in range(9):
		if com.lower() == complexity[i]: 
			if TLE(n, m, i):
				print("TLE")
			else:
				print("AC")
			break