s = input()
s = s.replace('+','')
l=list(map(int,s))
l.sort()
i=0
while(i<len(l)):
    if(i==(len(l)-1)):
        print(l[i],end='')
    else:
        print(l[i],end='+')
    i+=1