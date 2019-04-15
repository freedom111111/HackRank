n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())

for s in numbers:
    if s[0] == s:
        print('NO')
    else:
        for i in range(1,len(s)):
            mystack = [s[:i]]
#            print(mystack)
            while len(''.join(mystack))<len(s):
                mystack.append(str(int(mystack[-1])+1))
            if ''.join(mystack) == s:
                print('YES',mystack[0])
                break
#                print(mystack[0])
            if i == len(s)-1:
                print('NO')

