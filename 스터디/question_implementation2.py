#문자열 재정렬
S=input()
char=''
num=0
for i in S:
    if i in '0123456789':
        num+=int(i)
    else:
        char=char+i
answer=''.join(sorted(char))+str(num)
print(answer)
