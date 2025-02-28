from setup import *

# WordHunt Game Board
class WordHuntInstance():

    # Board Setup
    def __init__(self):
        self.gameBoard = []
        for i in range(4):
            self.gameBoard.append([''for x in range(4)])
    def __str__(self):
        return(str(self.gameBoard))

    # Sets board based on user input
    def setBoard(self,*letters):
        if len(letters) != 16:
            return
        for row in range(4):
            for item in range(4):
                self.gameBoard[row][item] = letters[row*4+item]
        return self.gameBoard

# Stores Tile Information
class Node():

    # Define all moves from the tile
    directionList = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if not (dr == 0 and dc == 0)]

    # Creates Node
    def __init__(self,board,currentword,position ,visitedtiles, parent, move,starting=None):
        self.boardState = board # 4x4 array
        self.currentWord = currentword #C urrent Word
        self.location = position # Tuple (row,column)
        self.visitedTiles = visitedtiles # 4x4 array
        self.parentNode = parent # gives parent node
        self.move = move # gives a tuple (x,y) where x and y are either -1,0,1
        self.children = [] # Keeps track of all neighboring children
        self.startingCell = starting # Keeps track of starting Node in the chain

    # Returns list of all neighboring tiles
    def getNeighbors(self):
        neighbors = []
        row,column = self.location[0],self.location[1]
        for index,(dx,dy) in enumerate(self.directionList):
            if row+dx < 4 and column+dy < 4:
                if row+dx>-1 and column+dy>-1:
                    if not self.visitedTiles[column+dy][row+dx]:
                        neighbors.append((dx,dy))
        return neighbors


    def makeChildNode(self,move):
        newX,newY = self.location[0]+move[0],self.location[1]+move[1]
        newWord = self.currentWord + self.boardState[newY][newX]
        newVisited = [row[:]for row in self.visitedTiles]
        newVisited[newY][newX] = True
        newChild = Node(self.boardState,newWord,(newX,newY),newVisited,self,move)
        self.children.append(newChild)
        return newChild


    def checkWord(self):
        return self.currentWord in wordlist

    def checkPrefix(self):
        return word_trie.has_prefix(self.currentWord)

    def getPath(self):
        if self.parentNode != None:
            return self.parentNode.getPath() + [self.move]
        else:
            return [self.startingCell]


# Responsible for the order of the candidate tiles to be checked
class QueueFrontier():

    # Initialize empty Queue
    def __init__(self):
        self.queue = []

    # Add term to Queue
    def addTerm(self,item):
        self.queue.append(item)

    # Remove term from Queue
    def removeTerm(self):
        return self.queue.pop(0)

    # Check if Queue is empty
    def isEmpty(self):
        return len(self.queue) == 0


