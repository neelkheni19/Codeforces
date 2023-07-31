n,k = map(int,input().split())
m=0
x = list(map(int,input().split()))
for j in range(len(x)):
    if(x[j]>=x[k-1] and x[j]>0):
        m+=1      
    

print(m)