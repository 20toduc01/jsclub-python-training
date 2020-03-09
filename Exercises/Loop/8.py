#Tìm đọc về thuật toán sắp xếp đơn giản
N = int(input())
a = []
for i in range(N):
	bf = int(input())
	a.append(bf)

for i in range(N - 1):
	for j in range(i + 1, N):
		if a[i] > a[j]:
			t = a[i]
			a[i] = a[j]
			a[j] = t
print(a)