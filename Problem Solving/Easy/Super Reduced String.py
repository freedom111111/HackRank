s = str(input())
#print(s)

i = 0 
res = []
for c in s:
    if res and res[len(res)-1]==c:
        res.pop()
    else:
        res.append(c)
print(''.join(res)) if res else print('Empty String')
