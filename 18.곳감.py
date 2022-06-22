n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
z = int(input())

sum = 0
# 회전
for i in range(z):
    h, t, k = map(int, input().split())  # h = 행, t = 방향(왼,오른), k = 이동 수

    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))

    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

# 중간체크
# for x in a:
#     print(x)

# 합산
start = 0
end = n-1
sum = 0
for i in range(n):
    for j in range(start, end+1):
        sum += a[i][j]

    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(sum)
