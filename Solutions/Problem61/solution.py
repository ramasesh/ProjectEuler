
import numpy as np

#triangular numbers are defined by Tn = n(n+1)/2, or n^2+n-2x=0
minTri =  int(np.ceil((-1 + np.sqrt(1**2 - 4*1*(-2*1000))) / (2 * 1)))
maxTri =  int(np.ceil((-1 + np.sqrt(1**2 - 4*1*(-2*10000))) / (2 * 1)))
triangles = [i*(i+1)/2 for i in range(minTri,maxTri)]
triangles_head = [i/100 for i in triangles]

#square numbers are defined by Sn = n^2, or
minSq =  32
maxSq =  100
squares = [i**2 for i in range(minSq,maxSq)]
squares_head = [i/100 for i in squares]
squares_tail = [i%100 for i in squares]


#pentagonal numbers are defined by n(3n-1)/2  = x, or 3n^2 - n - 2x = 0
minPent =  int(np.ceil((1 + np.sqrt(1**2 - 4*3*(-2*1000))) / (2 * 3)))
maxPent =  int(np.ceil((1 + np.sqrt(1**2 - 4*3*(-2*10000))) / (2 * 3)))
pents = [i*(3*i-1)/2 for i in range(minPent,maxPent)]
pents_head = [i/100 for i in pents]
pents_tail = [i%100 for i in pents]

#hexagonal numbers are defined by n(2n-1)  = x, or 2n^2-n - x = 0
minHex =  int(np.ceil((1 + np.sqrt(1**2 - 4*2*(-1000))) / (2 * 2)))
maxHex =  int(np.ceil((1 + np.sqrt(1**2 - 4*2*(-10000))) / (2 * 2)))
hexes = [i*(2*i-1) for i in range(minHex,maxHex)]
hexes_head = [i/100 for i in hexes]
hexes_tail = [i%100 for i in hexes]

#heptagonal numbers are defined by n(5n-3)/2 = x, or 5n^2-3n-2x=0
minHept = int(np.ceil((3 + np.sqrt(3**2 - 4*5*(-2*1000))) / (2 * 5)))
maxHept = int(np.ceil((3 + np.sqrt(3**2 - 4*5*(-2*10000))) / (2 * 5)))
hepts = [i*(5*i-3)/2 for i in range(minHept,maxHept)]
hepts_head = [i/100 for i in hepts]
hepts_tail = [i%100 for i in hepts]

#octagonal numbers are defined by n(3n-2) = x, or 3n^2-2n-x=0
minOct = int(np.ceil((2 + np.sqrt(2**2 - 4*3*(-1000))) / (2 * 3)))
maxOct = int(np.ceil((2 + np.sqrt(2**2 - 4*3*(-10000))) / (2 * 3)))
octs = [i*(3*i-2) for i in range(minOct,maxOct)]
octs_head = [i/100 for i in octs]
octs_tail = [i%100 for i in octs]

count = 0
for i in range(len(octs)):
    if (octs_tail[i] in hepts_head):
        print('Hepts:  {} {}'.format(octs[i],hepts[hepts_head.index(octs_tail[i])]))
        count+=1
    if (octs_tail[i] in hexes_head):
        print('Hexes:  {} {}'.format(octs[i],hexes[hexes_head.index(octs_tail[i])]))
        count+=1
    if (octs_tail[i] in pents_head):
        print('Pents:  {} {}'.format(octs[i],pents[pents_head.index(octs_tail[i])]))
        count+=1
    if (octs_tail[i] in squares_head):
        print('Squares:  {} {}'.format(octs[i],squares[squares_head.index(octs_tail[i])]))
        count+=1
    if (octs_tail[i] in triangles_head):
        print('Triangles:  {} {}'.format(octs[i],triangles[triangles_head.index(octs_tail[i])]))
        count+=1



