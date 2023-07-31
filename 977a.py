l = list(map(int,input().split()))
n = l[0]
k = l[1]
for i in range(k):
    if(n%10 != 0):
        n-=1
    else:
        n//=10
print(n)