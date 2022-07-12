a = "aaabbccccdd"
i = 0
msg = ""
while i < len(a):
    count = 1
    x = a[i]
    j = i
    while j < len(a)-1:
        if a[j] == a[j+1]:
            count += 1
        else:
            break
        j += 1
    msg = msg + x + str(count) 
    i = j + 1
print(msg)

