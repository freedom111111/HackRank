def findDigits(n):
    str_digit = str(n)
    count = 0
    for i in range(len(str_digit)):
        num = int(str_digit[i])
        if num ==0 :
            continue
        else:
            if n % num ==0:
                count +=1
    return count
