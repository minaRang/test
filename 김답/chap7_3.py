print("떡의 개수와 요청할 떡의 길이 입력 : ", end='');n,m=map(int,input().split())
print("떡의 개별 높이 입력:", end='');lengths=list(map(int,input().split()))

def search(start,end,target,array):
    h=0
    #이진 탐색
    while start<=end:
        mid = (start + end) // 2
        m = 0
        #잘랐을 때 떡의 길이를 구함
        for length in array:
            if mid<length:
                m+=(length-mid)
        #잘랐을 때 떡의 길이가 목표 길이보다 모자라면 자르는 길이를 줄인다
        if m<target:
            end=mid-1
        #잘랐을 때 떡의 길이가 목표 길이보다 남으면 자르는 길이를 늘린다
        else:
            start=mid+1
            h=mid
    return h

print("절단기의 최대 높이:", search(1,max(lengths),m,lengths))