noOfCities = int(input("Enter Number of cities to be visited: "))
initial =[0,0]  
final = [0,0]

def checkBlock (initialPos, finalPos, block, head):  #function to check if there is a block in the path
    if head == 'E' and block[1] == initialPos[1]:
        for x in range (initialPos[0], finalPos[0]):
            if x == block[0]:
                return True
    elif  head == 'N' and block[0] == initialPos[0]:
        for y in range (initialPos[1], finalPos[1]):
            if y == block[1]:
                return True
    elif head == 'W' and block[1] == initialPos[1]:
        for x in range (finalPos[0], initialPos[0]):
            if x == block[0]:
                return True 
    elif head == 'S' and block[0] == initialPos[0]:
        for y in range (finalPos[1], initialPos[1]):
            if y == block[1]:
                return True


def path (dir, edge, x, y, pathway):   #function that prints the path which traveller is following
    isBlock = 0
    if x == 0 and y== 0 and len(pathway) == maxEdge:
        initial = [0,0]
        final = [0,0]
        for i in range(1, len(pathway)+1):
            
            head = pathway[i-1]
    
            if head == 'E':
                final[0] = final[0] + i
            elif head == 'W':
                final[0] = final[0] - i
            elif head == 'N':
                final[1] = final[1] + i
            else:
                final[1] = final[1] - i            
            
            for j in range (0, len(blocks)):
                if checkBlock(initial, final, blocks[j], head) :   #checking if there is any block in path
                    isBlock = 1  
                    
            initial = [x for x in final]    
        
        if  isBlock != 1:    
            print("possible paths to travel: ", end = '')        
            print(''.join(pathway))
            totalPath.append(pathway)
        
        return

    if edge >= maxEdge: 
        return

    elif dir == 'E' or dir == 'W':
        pathway.append('N')
        path('N', edge+1, x, y+(edge+1),pathway)   #calling function recursively
        pathway.pop()
        pathway.append('S')
        path('S', edge+1, x, y-(edge+1),pathway)
        pathway.pop()
    
    else:
        pathway.append('E')
        path('E', edge+1, x+edge+1, y,pathway)
        pathway.pop()
        pathway.append('W')
        path( 'W', edge+1, x-(edge+1), y,pathway) 
        pathway.pop()


for  i in range(1, noOfCities+1):
    blocks = []
    print("\nFor city " + str(i))

    maxEdge = int(input("Enter maximum edge : "))
    noOfBlocks = int(input("Enter No. of blocks: "))
    print("Enter x and y coordinates for " + str(noOfBlocks) + "  blocks: ")
    for i in range(noOfBlocks):
        blocks.append([int(x) for x in input().split()])

    totalPath = []   #list which stores all possible paths of travel

    #Considering west as first move         
    pathway=[]   #list which stores possible paths for a direction
    pathway.append('W')
    path('W', 1, -1, 0, pathway)
    
    #Cosidering east as first move:
    pathway = []
    pathway.append('E')
    path('E', 1, 1, 0, pathway)
    
    #Considering north as first move: 
    pathway = []  
    pathway.append('N')
    path('N', 1, 0, 1, pathway)
    
    #Considering south as first move: 
    pathway = []
    pathway.append('S')
    path('S', 1, 0, -1, pathway)

    
    print("Found " + str(len(totalPath)) + " golygon(s)")  #prints number of golygons
