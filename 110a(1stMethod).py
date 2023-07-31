n = int(input())
count=0
for i in range(n):
    if(n%10 == 4 or n%10==7):
        count+=1
    n//=10
    if(n<1):
        break
 
bul = False
for i in range(count):
    if(count%10==4 or count%10==7):
        bul=True
    else:
        bul=False
        break
if(bul==True):
    print('YES')
else:
    print('NO')
 
