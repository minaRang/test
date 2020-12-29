count = 0
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
input_data=input()
row = int(input_data[1])
column = int(ord(input_data[0])) -  int(ord('a')) + 1
#ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
#다른 분들 코드도 참고하고 싶은 부분임

for step in steps:
    nrow = row+step[0]
    ncolumn = column+step[1]
    if (nrow >=1 and nrow <=8) and (ncolumn>=1 and ncolumn<=8):
        count +=1
        
print(count)