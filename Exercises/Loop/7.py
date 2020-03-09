N = int(input())
a = []
for i in range(N):
	bf = int(input())
	a.append(bf)

for i in range(N):
	if a[i] % 2 == 0:
		print(a[i])