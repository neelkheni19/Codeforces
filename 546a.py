l = list(map(int,input().split()))
k = l[0]
n = l[1]
w = l[2]

cost = w*(w+1)//2*k
print(cost-n)