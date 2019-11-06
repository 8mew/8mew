def buildWalsh( walsh , l , i1 , i2 , j1 , j2 , bar ):

    if l == 2:

        one = -1 if bar else 1

        walsh[i1][j1] = one
        walsh[i1][j2] = one
        walsh[i2][j1] = one
        walsh[i2][j2] = -one

        return


    midi = (i1+i2)//2
    midj = (j1+j2)//2

    nl = l//2 # its L not 1

    buildWalsh( walsh , nl, i1, midi, j1, midj, bar)
    buildWalsh( walsh , nl, i1, midi, midj + 1, j2, bar)
    buildWalsh( walsh , nl, midi + 1, i2, j1, midj, bar) 
    buildWalsh( walsh , nl, midi + 1, i2, midj + 1, j2, not bar)

def showWalsh(walsh):
    print("*********")
    print("Walsh Table")
    for w in walsh:
        print(*w)
    print("*********")


def setup( walsh , chnlSeq ,  data ):

    for i , d in enumerate( data ):
        w = dotMul( walsh[i] , d)
        chnlSeq = addMat( chnlSeq  , w )

    print("Channel Sequence is: " , *chnlSeq)
    return chnlSeq


def listenTo( walsh , chnlSeq , source ):

    print("Listening to Channel", source)
    inner = sum(innerProd( walsh[source-1] , chnlSeq ))
    print("Data recieved is: " , inner//stations)
        
def addMat(am , bm):
    nm = []
    for a , b in zip(am , bm):
        nm.append(a+b)
    return nm

def dotMul(am , c):
    nm = []
    for a in am:
        nm.append( a*c )
    return nm

def innerProd(am , bm):
    nm = []
    for a , b in zip(am , bm):
        nm.append(a*b)
    return nm

stations = 4
walsh = [ [0 for _ in range (stations) ] for __ in range(stations) ]
chnlSeq =  [0 for _ in range (stations) ]
data = []
for i in range(4):
	print("Enter Data for Station : ",i+1)
	d = int(input())
	data.append(d)		
buildWalsh( walsh, 4,  0 , 3 , 0 , 3 , False)
showWalsh(walsh)
chnlSeq = setup( walsh , chnlSeq , data )
print("Resultant Channel Sequence : ",chnlSeq)
print("Enter the channel number who's data you wish to receive : ")
n = int(input()) 
listenTo( walsh , chnlSeq , n )

'''
universe@hp4:~/Downloads$ python3 cdma.py 
Enter Data for Station :  1
1
Enter Data for Station :  2
-1
Enter Data for Station :  3
0
Enter Data for Station :  4
1
*********
Walsh Table
1 1 1 1
1 -1 1 -1
1 1 -1 -1
1 -1 -1 1
*********
Channel Sequence is:  1 1 -1 3
Resultant Channel Sequence :  [1, 1, -1, 3]
Enter the channel number who's data you wish to receive : 
2
Listening to Channel 2
Data recieved is:  -1
universe@hp4:~/Downloads$
'''
