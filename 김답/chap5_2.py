n=int(input("수열에 속해있는 수의 개수는? "))

#n개의 정수 입력받음
array=[]
for _ in range(n):
    array.append(int(input("수 입력:")))

#계수정렬
count=[0]*(max(array)+1)
for i in range(len(array)):
    count[array[i]]+=1

#정렬 결과를 역순으로 출력
for i in range(len(count)-1,0,-1):
    for j in range(count[i]):
        print(i,end=' ')