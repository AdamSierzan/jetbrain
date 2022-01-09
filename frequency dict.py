from collections import Counter
a = "a aa abC aa ac abc bcd a".lower().split()
b = Counter(a)
print(b)
for i, e  in b.items():
    print(i,e)
print(a)
for i in a:
    dict = {i: i.count(i)for i in a}

print(dict)