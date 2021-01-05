n = int(input())
d = [0] * 1001

#바텀업은 아무래도 점화식 세우면 되는거 같다.
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) %796796

print(d[n])