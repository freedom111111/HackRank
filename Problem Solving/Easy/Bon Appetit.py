def bonAppetit(bill, k, b):
    
    bill.pop(k)
    total = sum(bill)
    share = total/2
    if share == b:
        print('Bon Appetit')
    elif share<b:
        print(int(b-share))
