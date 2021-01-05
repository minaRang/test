d = [0] * 100 #0으로 배열 초기화 100개

def fibo(x):
    #종료 조건
    if x == 1 or x == 2:
        return 1
    #계산한 적 있으면
    if d[x] != 0:
        return d[x]
    #계산 아직 안했으면
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

#시작복잡도가 O(n)인데 이 부분이 잘 이해가 가지 않는다. fibo(x-1)을 먼저 계산하면서 내려가서인가? 아님 return값?
#계산한 적 있다면 재귀 호출 없이 바로 리턴해버려서 (문제개수 * 문제 1개 푸는 시간)
"""
재귀 함수로 썼을때는
def fibo(x):
    if x ==1 or x == 2:
        return 1
    return fibo(x-1)+fibo(x-2)

이며 시간 복잡도는 O(2^N)
"""