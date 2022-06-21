n = int(input())
m = int(input())
a = list(map(int, input().split()))
# a = [1, 2, 1, 3, 1, 1, 1, 2]
tot = a[0]
count = 0
rt = 1
lt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1

        else:
            break

    elif tot == m:
        count += 1
        tot -= a[lt]
        lt += 1

    else:
        tot -= a[lt]
        lt += 1

print(count)
