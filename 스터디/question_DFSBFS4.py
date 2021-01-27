#괄호 변환
def balance(string):
    count=0
    for i in string:
        if i=='(':
            count+=1
        else:    
            count+=1
    if count==0:
        return True
    else:
        return False
def correct(string):
    stack=[]
    for letter in string:
        if (not stack) or stack[-1]==letter:
            stack.append(letter)
        else:
            stack.pop()
    if stack:
        return True
    else:
        return False
            
            
def solution(p):
    for i in range(len(p)):
        if balance(p[:i]):
            u=p[:i]
            v=p[i:]
            break
    if correct(u):
        return u+solution(v)
    else:
        return '('+solution(v)+')'+u[1:-1:-1]