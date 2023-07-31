s = input()
count_lower = 0
count_upper = 0
for i in range(len(s)):
    if(s[i].isupper() == True):
        count_upper+=1
    elif(s[i].islower() == True):
        count_lower+=1
if(count_lower>=count_upper):
    print(s.lower())
else:
    print(s.upper())