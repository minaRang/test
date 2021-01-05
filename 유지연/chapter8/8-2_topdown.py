n = int(input())
d = list(map(int, input().split()))
#d = [0] * 1000 #초기화과정 -> 여기선 굳이 안필요하지 않나요..?

def f(n):
    if n==0:
        return d[0]
    if n==1:
        return d[1]
    result1 = d[n-1] + f(n-3)
    result2 = d[n-2] + f(n-4)
    result = max(result1, result2)
    return result


print(f(n))


