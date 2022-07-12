def PairSum(A, X):
    i = 0
    j = len(a)-1
    while i < j:
        if A[i] + A[j] == X:
            return True
        elif A[i] + A[j] < X:
            i += 1
        else:
            j -= 1
    return 0

a = [2, 3, 5, 8, 10, 11, 7]
val = 17
print(PairSum(a, val))