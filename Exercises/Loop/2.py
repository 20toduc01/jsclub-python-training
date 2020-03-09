N = int(input())
for i in range(2, N):
	if N % i == 0:
		print("N không phải số nguyên tố")
		exit()
print(N, "là số nguyên tố")
