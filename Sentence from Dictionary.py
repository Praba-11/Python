string = "iloveamazon"
res = ""
dictionary = {1: "i", 2:"love", 3:"amazon"}
for i in dictionary.values():
    if i in string:
        res += (i+" ")
print(res)