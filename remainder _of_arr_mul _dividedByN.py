arr = [100, 103, 56, 25, 35, 14];lens = len(arr);n = 11
mul = 1
for i in range(lens):
	mul = (mul * (arr[i] % n)) % n
print(mul % n)
