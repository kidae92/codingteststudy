a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((s+e+1)):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
