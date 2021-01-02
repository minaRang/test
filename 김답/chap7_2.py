n=int(input("동빈이네 전자 매장의 부품 개수는? : "))
print("부품 번호 입력 ",end='');ns=list(map(int,input().split()))
m=int(input("확인할 부품의 수는? : "))
print("부품 번호 입력 ",end='');ms=list(map(int,input().split()))

ns.sort()

def search(start,end,target,array):
    mid=(start+end)//2
    while start<=end:
        if array[mid]==target:
            return "yes"
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
        mid=(start + end) // 2
    return "no"

for i in ms:
    print(search(0,n-1,i,ns),end=' ')