
n = int(input())
i=0
while(i<n):
    st = input()
    if(len(st)>10):
        print(st[0],len(st)-2,st[len(st)-1])
    else:
        print(st)
    i+=1
    


