
#문자열 S, 알파벳값 정렬시킬 빈 정렬 result, 숫자 더할 값 sum
s=input()
result=[]
sum=0

#아스키 코드 사용하려고 했으나 함수 isalpha, isdigit 존재
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum+=int(i)

result.sort()
result.append(str(sum))

#오류떠서 각각 int, str로 캐스팅 해줌

print(''.join(result))
