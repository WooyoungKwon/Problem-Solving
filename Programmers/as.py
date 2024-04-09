counts = dict()
names = ['a', 'b', 'a', 'c', 'd']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)