n, m = map(int, input().split())

max = 0
count = [0] * (m+n+3)
for i in range(1, n+1):
    for j in range(1, m+1):
        count[i+j] += 1

for i in range(n+m+1):
    if count[i] > max:
        max = count[i]

for i in range(n+m+1):
    if count[i] == max:
        print(i, end=' ')
