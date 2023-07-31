n = int(input())
j=[]
i=0
while(i<n):
    x = list(map(int,input().split()))
    if(sum(x) > 1):
        j.append(1)
    else:
        j.append(0)
    i+=1
print(sum(j))