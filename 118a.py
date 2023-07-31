s = input().lower()

s = '.'.join([i for i in s if not i in "aeiou"])
print('.'+s)