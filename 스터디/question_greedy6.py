def solution(food_times, k):
    l=len(food_times)
    eats=list(range(l))
    clk=0
    for _ in range(k):
        if not eats:
            return -1
        food=clk//l
        if food_times[food]==0:
            eats.pop(food)
        else:
            food_times[food]-=1
            clk+=1
    return food
#해결 못함