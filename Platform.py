arrival = [2.00, 2.40, 2.50, 4.00, 8.00, 11.00]
departure = [2.10, 5.00, 4.20, 4.30, 12.00, 12.40]
arrival.sort()
departure.sort()
n1 = len(arrival)
n2 = len(departure)
i = 0
j = 0
platform = 0
result = 0
while(i<n1 and j<n2):
    if arrival[i] < departure[j]:
        i += 1
        platform += 1
    else:
        j += 1
        platform -= 1
    if result < platform:
        result = platform
print("Minimum platforms required: ", result)