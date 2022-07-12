s = "codewordaccepted"
n = len(s)
i = 0
c = []
res = ""
while i < n:
    e = []
    j = i
    while j < n:
        if s[j] not in e:
            e.append(s[j])
        else:
            break
        j += 1
    b = i
    i = j
    if len(res) < len(s[b:i]):
        res = s[b:i]
print(res)
    

