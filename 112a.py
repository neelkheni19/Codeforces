l = input().lower()
u = input().lower()
s=[]
r=[]
rs=[]
b=True
for i,j in zip(l,u):
    s.append(ord(i)-96)
    r.append(ord(j)-96)

for i in range(len(s)):
    rs.append(s[i]-r[i])
for i in range(len(rs)):
    if(rs[i]==0):
        b=False
        continue
    if(rs[i]<0):
        print(-1)
        b=True
        break
    if(rs[i]>0):
        print(1)
        b=True
        break
if(b==False):
    print(0)


