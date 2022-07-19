def left_r(a, key):
    res = a[key:] + a[0:key]
    return res
def right_r(a, key):
    res = left_r(a, len(a)-key)
    return res


a = "HELLOLOLLLLOO!"
key = 3
print(left_r(a, key))
print(right_r(a, key))