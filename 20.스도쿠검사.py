
a = [list(map(int, input().split())) for _ in range(9)]


def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False


if check(a):
    print("yes")
else:
    print("no")
