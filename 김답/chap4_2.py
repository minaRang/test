n=int(input("몇 시까지? :"))
count=0

for h in range(n+1) :
    #시간에 3이 포함되어 있다면 분, 초에 상관없이 무조건 센다.
    if h//10==3 or h%10==3:
        for m in range(60):
            for s in range(60):
                count += 1
    # 시간에 3이 포함되어 있지 않다면
    else :
        # 분에 3이 포함되어 있는지 확인한다.
        for m in range(60):
            
            # 분에 3이 포함되어 있다면 초에 상관없이 무조건 센다.
            if m // 10 == 3 or m % 10 == 3:
                for s in range(60):
                    count += 1
            # 분에 3이 포함되어 있지 않다면 초에 3이 있는 경우만 센다.
            else:
                for s in range(60):
                    if s // 10 == 3 or s % 10 == 3:
                        count += 1

print(count)