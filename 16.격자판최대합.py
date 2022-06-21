n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000


for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

        if sum1 > largest:
            largest = sum1

        if sum2 > largest:
            largest = sum2
print(largest)
sum3 = sum4 = 0
for i in range(n):
    sum3 += a[i][i]
    sum4 += a[i][n-i-1]


if sum3 > largest:
    largest = sum3

if sum4 > largest:
    largest = sum4


print(largest)
