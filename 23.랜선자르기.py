k, n = map(int, input().split())
line = []
res = 0
largest = 0


def Count(len):
    count = 0
    for x in line:
        count += (x // len)
    return count


for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

left = 1
right = largest

while left <= right:
    mid = (left + right) // 2
    if Count(mid) >= n:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
