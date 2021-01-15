S=input()
count=0
if S[0]=='1':
    key='10'
if S[0]=='0':
    key='01'
for i in range(len(S)):
    if S[i:].startswith(key):
        count+=1
print(count)