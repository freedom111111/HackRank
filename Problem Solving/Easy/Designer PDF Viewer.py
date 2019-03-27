def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    width = len(word)
    height = 0
    for i in range(width):
        aa = word[i]
        ind = alphabet.index(aa)
        ht = h[ind]
        if ht >= height:
            height = ht
            
    return height*width
