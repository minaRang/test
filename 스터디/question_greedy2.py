numbers=input().lstrip('0')
result=int(numbers[0])
for number in numbers[1:]:
    number=int(number)
    if number==0 or number==1:
        result+=number
    else:
        result*=number
print(result)