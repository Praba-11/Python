def subarray(arr, start, end):
    if end == len(arr):
        return 
    elif start > end:
        return subarray(arr, 0, end + 1)
    else:
        a.append(arr[start:end+1])
        return subarray(arr, start + 1, end)

arr = [1, 2, 3, 4]
a = []
subarray(arr, 0, 0)
print(a)

for i in range(len(arr)+1):
    for j in range(i):
        print(arr[j:i])
