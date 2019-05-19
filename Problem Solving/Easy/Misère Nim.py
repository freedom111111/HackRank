 def misereNim(s):
    n= len(s)
    if set(s) == {1} and n%2:
        return 'Second'
    elif set(s) == {1} and not n%2:
        return 'First'
    elif reduce((lambda x,y:x^y),s):
        return 'First'
    else:
        return 'Second'
