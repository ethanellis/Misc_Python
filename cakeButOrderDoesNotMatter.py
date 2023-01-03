
#Did this in response to a Google challenge:

#Commander lambda has had an incredibly successful week:
#she completed the first test run of her LAMBCHOP doomsday device, she captured
#six key members of the Bunny Rebellion, and she beat her personal high score in Tetris.
#To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition
#among minions is fierce, and if you don't cut exactly equal slices of cake for everyone,
#you'll get in big trouble.

#The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest
#of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must
#get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not
#tolerate any leftovers, so you also want to make sure you can serve the entire cake.

#To help you best cut the cake, you have turned the sequence of colors of M&Ms on the cake
#into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence
#of M&Ms is given clockwise (the decorations form a cirlce around the outer edge of the cake).

#Write a function that, given a non-empty string less than 200 characters in length describing
#the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake
#without leaving any leftovers.

cake = "abcdefghiidcbefghaihgfedcba"

def slicer(cake):
    numPieces = 2
    maxNum = 1
    while numPieces <= len(cake):
        numPiecesWorks = True
        if len(cake) % numPieces == 0:
            for i in range(numPieces):
                pieceLength = int(len(cake)/numPieces)            
                if i>0:
                    slice1 = cake[i*pieceLength:(i+1)*pieceLength]
                    slice2 = cake[(i-1)*pieceLength:i*pieceLength]
                    for l in slice1:
                        if l in slice2:
                            continue
                        else:
                            numPiecesWorks = False
            if numPiecesWorks:
                maxNum = numPieces
        numPieces+=1
    return maxNum


#another version that doesn't use a while loop
def slicer2(cake):
    maxNum = 1
    for i in range(len(cake)):
        numPiecesWorks = True
        if i > 0:
            if len(cake)%i == 0:
                pieceLength = int(len(cake)/i)
                for x in range(i):
                    if x>0:
                        slice1 = cake[x*pieceLength:(x+1)*pieceLength]
                        slice2 = cake[(x-1)*pieceLength:x*pieceLength]
                        for l in slice1:
                            if l in slice2:
                                continue
                            else:
                                numPiecesWorks = False
                if numPiecesWorks:
                    maxNum = i
    return maxNum
