#main

#create a 6x8 array to hold variables

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
