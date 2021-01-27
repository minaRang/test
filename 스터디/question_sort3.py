def solution(N, stages):
    stages.sort()
    yet=[0]*N
    total=[]*N
    rate=[]*N
    for stage in stages:
        yet[stage-1]+=1
    for i in range(N):
        total[i]=sum(yet[i:])
        rate[i]=yet[i]/total[i]
    answer=[]
    for i in range(N):
        M=max(rate)
        i=rate.index(M)
        rate.pop(i)
        answer.append(i+1)
    return answer

#index error