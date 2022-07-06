a = [1, 3, 1, 2, 3, 5, 6, 8, 5, 4, 2, 4, 5, 6, 3, 2]
res = 0
n = len(a)
for i in range(1, n-1):
    if a[i-1] < a[i] > a[i+1]:
        left = right = i
        while left > 0 and a[left] > a[left-1]:
            left -= 1
        while right + 1 < n and a[right] > a[right+1]:
            right += 1
    res = max(res, right - left + 1)
print(res)