n = 'g0en2Ts8eSoft'

count = 0  # 약수의갯수
res = 0  # 숫자추출

for i in n:
    if i.isdecimal():
        res = res*10 + int(i)

print(res)

for i in range(1, res+1):
    if res % i == 0:
        count += 1

print(count)
