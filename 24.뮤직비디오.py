n, m = map(int, input().split())
music = list(map(int, input().split()))
left = 1
right = sum(music)
res = 0


def Count(capacity):
    count = 1
    sum = 0
    for x in music:
        if sum+x > capacity:
            count += 1
            sum = x
        else:
            sum += x

    return count


while left <= right:
    mid = (left+right)//2
    if Count(mid) <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)
