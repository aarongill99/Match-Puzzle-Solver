#main
import numpy as np
#create a 6x8 array to hold variables

#board = []
#board = numpy.arange(48).reshape((8, 6)) 
#board[1][1] = 3
#print(board)
#print(board[1][1])

board = np.array([[4,2,4,3,1,2],[4,2,2,3,2,3],[1,1,2,4,2,1],[1,4,3,1,3,2],[3,1,2,1,1,2],[2,2,3,2,2,3],[1,2,4,1,1,1],[1,2,3,2,3,1]])
print(board)




#in the array use refrences for colors/names
# 0 = Missing Tile (only used in part 2 of the algorithm)
# 1 = blue/bubbles
# 2 = green/leaves
# 3 = yellow/jar
# 4 = red/snake



# iterate through the array and check all 8 positions 
# if currTile = checkTile then add +1 to nearMatches count
# if nearMatches >= 2 then not a starting point probably*()
# if nearMatches = 0 then point has no partners

print(board[:,5])




#Sides

#board[0,:] = top row
for y in range(1,5):
    x = 0
    print("Checking position: [" + str(x) + "," + str(y) + "]")
    if board[x,y-1] == board[x,y]: #check top middle matching
        print("Middle Left match")
    if board[x,y+1] == board[x,y]: #check bottom middle matching
        print("Middle Right match") 
    if board[x+1,y-1] == board[x,y]: #check top right corner matching
        print("Bottom Left Corner match")
    if board[x+1,y] == board[x,y]: #check middle right matching
        print("Bottom Middle match")
    if board[x+1,y+1] == board[x,y]: #check bottom right corner matching
        print("Bottom Right Corner match")

#board[7,:] = bottom row 
for y in range(1,5):
    x = 7
    print("Checking position: [" + str(x) + "," + str(y) + "]")
    if board[x-1,y-1] == board[x,y]: #check top left corner matching
        print("Top Left Corner match")
    if board[x-1,y] == board[x,y]: #check middle left  matching
        print("Top Middle match")
    if board[x-1,y+1] == board[x,y]: #check bottom left corner matching
        print("Top Right Corner match")
    if board[x,y-1] == board[x,y]: #check top middle matching
        print("Middle Left match")
    if board[x,y+1] == board[x,y]: #check bottom middle matching
        print("Middle Right match") 

#board[:,0] = left column 
for x in range(1,7):
    y = 0
    print("Checking position: [" + str(x) + "," + str(y) + "]")
    if board[x-1,y] == board[x,y]: #check middle left  matching
        print("Top Middle match")
    if board[x-1,y+1] == board[x,y]: #check bottom left corner matching
        print("Top Right Corner match")
    if board[x,y+1] == board[x,y]: #check bottom middle matching
        print("Middle Right match") 
    if board[x+1,y] == board[x,y]: #check middle right matching
        print("Bottom Middle match")
    if board[x+1,y+1] == board[x,y]: #check bottom right corner matching
        print("Bottom Right Corner match")


#board[:,5] = right column 
for x in range(1,7):
    y = 5
    print("Checking position: [" + str(x) + "," + str(y) + "]")
    if board[x-1,y-1] == board[x,y]: #check top left corner matching
        print("Top Left Corner match")
    if board[x-1,y] == board[x,y]: #check middle left  matching
        print("Top Middle match")
    if board[x,y-1] == board[x,y]: #check top middle matching
        print("Middle Left match")
    if board[x+1,y-1] == board[x,y]: #check top right corner matching
        print("Bottom Left Corner match")
    if board[x+1,y] == board[x,y]: #check middle right matching
        print("Bottom Middle match")







#Corners

#board[0,0] = top left corner
print("Checking position: [0,0]")
if board[0,1] == board[0,0]: #check bottom middle matching
    print("Middle Right match")
if board[1,0] == board[0,0]: #check middle right matching
    print("Bottom Middle match")
if board[1,1] == board[0,0]: #check bottom right corner matching
    print("Bottom Right Corner match")

#board[0,5] = top right corner
print("Checking position: [0,5]")
if board[0,5-1] == board[0,5]: #check top middle matching
    print("Middle Left match")
if board[0+1,5] == board[0,5]: #check middle right matching
    print("Bottom Middle match")
if board[0+1,5-1] == board[0,5]: #check top right corner matching
    print("Bottom Left Corner match")

#board[7,0] = bottom left corner
print("Checking position: [7,0]")
if board[7-1,0] == board[7,0]: #check middle left  matching
    print("Top Middle match")
if board[7-1,0+1] == board[7,0]: #check bottom left corner matching
    print("Top Right Corner match")
if board[7,0+1] == board[7,0]: #check bottom middle matching
    print("Middle Right match") 

#board[7,5] = bottom right corner
print("Checking position: [7,5]")
if board[7-1,5] == board[7,5]: #check middle left  matching
    print("Top Middle match")
if board[7,5-1] == board[7,5]: #check top middle matching
    print("Middle Left match")
if board[7-1,5-1] == board[7,5]: #check top left corner matching
    print("Top Left Corner match")



#Middle


for x in range(1,6):
    for y in range(1,4):
        print("Checking position: [" + str(x) + "," + str(y) + "]")
        if board[x-1,y-1] == board[x,y]: #check top left corner matching
            print("Top Left Corner match")
        if board[x-1,y] == board[x,y]: #check middle left  matching
            print("Top Middle match")
        if board[x-1,y+1] == board[x,y]: #check bottom left corner matching
            print("Top Right Corner match")
        if board[x,y-1] == board[x,y]: #check top middle matching
            print("Middle Left match")
        if board[x,y+1] == board[x,y]: #check bottom middle matching
            print("Middle Right match") 
        if board[x+1,y-1] == board[x,y]: #check top right corner matching
            print("Bottom Left Corner match")
        if board[x+1,y] == board[x,y]: #check middle right matching
            print("Bottom Middle match")
        if board[x+1,y+1] == board[x,y]: #check bottom right corner matching
            print("Bottom Right Corner match")
                    


    print("\n")
    




#could use a recursive tree
#if the currTile has more than 1 near matches then split into 2 and keep splitting until end of all tree's
#at the end of each finished split check if the branchScore > maxScore if true then overwrite the maxPath with the currPath and maxScore with branchScore
#after all the iterations are complete you should have the best maximum branch, then store this branch and path in memory (we do this for each point because for part 2 we need the top 5 or 10 branches to check)

#do the exact same thing for all 48 starting positions




# should probably try to use a modified version of the A* algorithm for path finding



#part 2 (implement after fully working part 1)
#using the top 5 or 10 branches found, run a simulation of what would happen if each of them was chosen
#basically for each of the branches chosen, remove all the positions used then fill them in from the tiles above them (this will give us a new table with the only unknown positions at the top)
#Calculate the maximum score possible for each branch now and store it as nextScore

#If nextScore + maxScore of the chosen branches is the largest of all of the top 5 or 10 then choose that path
