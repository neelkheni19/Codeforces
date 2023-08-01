m=[]
for i in range(1, 6):
    s = list(map(int, input().split()))
    m.append(s)
for i in range(len(m)):
    for j in range(len(m[i])):
                
        if (m[i][j] == 1):
            x = (abs(i-2) + abs(j-2))
            print(abs(x))
        
# if (m[4][4]==1):
#         print(4)
        
        