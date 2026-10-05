d = [14, 58, 84, 40, 25]

print(d)
total=0
for c in range(0, len(d)):
    total+=d[c]
    for j in range(len(d) - c - 1):
        if d[j] > d[j + 1]:
            temp = d[j]
            d[j] = d[j + 1]
            d[j + 1] = temp

print(d)
print(total)
print(f"{d[0]}is min element and {d[-1]} is max element")


