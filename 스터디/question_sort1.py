N=int(input())
table=[]
for _ in range(N):
    data=input().split()
    
    for i in range(1,4):
        data[i]=int(data[i])
    
    table.append(data)

table.sort(key=lambda student:(-student[1],student[2],-student[3],student[0]))
for student in table:
    print(student[0])