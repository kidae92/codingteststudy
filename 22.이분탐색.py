
target = int(32)
a = list(map(int, input().split()))
a.sort()

left = 0
right = len(a)-1


while left <= right:
    mid = (left+right) // 2
    if a[mid] == target:
        print(mid+1)
        break

    elif a[mid] < target:

        left = mid + 1

    else:
        right = mid - 1
