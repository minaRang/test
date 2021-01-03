#학생수 n을 입력받고 학생수만큼 이름, 성적을 받음
n=int(input("학생의 수는?: "))
student=[]
for _ in range(n):
    print("이름과 성적 입력 :",end='');student.append(tuple(map(str,input().split())))

def setting(data):
    return int(data[1])

student.sort(key=setting)

for s in student:
    print(s[0], end=' ')
