n = int(input())
count=0
for i in range(n):
    if(n%10 == 4 or n%10==7):
        count+=1
    n//=10
    if(n<1):
        break
    
res = str(count)


print('NO' if res not in '47' else 'YES')