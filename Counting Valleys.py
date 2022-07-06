n = "UDDDDUDUUUDDUUDU"
count = 0
valley = 0
for i in n:
    if i == 'U':
        count += 1
        if count == 0:
            valley += 1
        else:
            continue
    elif i == 'D':
        count -= 1
print("{} valleys.".format(valley))
