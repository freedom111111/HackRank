def taumBday(b, w, bc, wc, z):
    if bc > (wc+z):
        return w*wc+(wc+z)*b
    elif wc > (bc+z):
        return (bc+z)*w+b*bc
    else:
        return w*wc+b*bc
