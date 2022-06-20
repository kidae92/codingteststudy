n = int(input())
a = map(int, input().split())

po = 0
bo = 0

for i in a:
    if i == 1:
        bo += 1
        po += bo
    else:
        bo = 0
print(po)
