#고정점 찾기
N=int(input())
arr=list(map(int,input().split()))

def fixpoint(start,end,arr):
    if start>end:
        return -1
    index=(start+end)//2
    if arr[index]==index:
        return index
    elif arr[index]>index:
        return fixpoint(start,index-1,arr)
    else:
        return fixpoint(index+1,end,arr)

print(fixpoint(0,N,arr))