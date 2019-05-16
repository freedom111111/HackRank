#The justification is that the xor simulates binary addition without 
#the carry over to the next digit. For the zero digits of n you can 
#either add a 1 or 0 without getting a carry which implies xor = + whereas 
#if a digit in n is 1 then the matching digit in x is forced to be 0 
#on order to avoid carry. For each 0 in n in the matching digit in x 
#can either being a 1 or 0 with a total combination count of 2^(num of zero).


def sumXor(n):
    return 2**(bin(n)[2::].count("0")) if n!=0 else 1
