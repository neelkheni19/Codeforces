a = list(map(int,input().split()))
count = 0 

def abc(a,b,count):
    if(a>b):
        print(count)
    else:
        a = a*3
        b = b*2
        count+=1
        abc(a,b,count)
abc(a[0],a[1],count=count)