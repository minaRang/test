h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)                
   
#range(h+1) == range(0,h+1) 0부터 h까지 숫자 객체