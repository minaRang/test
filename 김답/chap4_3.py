k=input("나이트의 현재 위치는? : ")
count=0

for n in [-1,1]:
    for e in [-2,2]:
        if(0<(int(k[1])+n))and(ord('a')<=ord(k[0])+e<=ord('h')):
            count+=1
        if (0<(int(k[1]) + e)) and (ord('a') <= ord(k[0]) + n <= ord('h')):
            count+=1

print("나이트가 이동할 수 있는 경우의 수는" ,count)