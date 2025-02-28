from classes import *
from Main.functions import*

# New WordHunt game Instance
Game = WordHuntInstance()

# Get user input from Wordhunt game and sets up the board
letters = [*input("letters:").upper()]
Game.setBoard(*letters)

# Show board in console
print(Game.gameBoard)

# Setup nodes for Breadth First Search to find words.
wordNodes = []
wordsFound = set()
wordInstructions = {}

# Setup board size to 4x4
boardSize = 4

# Breadth First Search Algorithm to find all possible words
# Loops for every row starting from the top row and evey column starting from the left
for y in range(boardSize):
    for x in range(boardSize):

        nodeQueue = QueueFrontier() # Creates a Queue Frontier *DO LATER*
        startingCell = (x,y) # Sets starting cel to current cell

        # Sets up the starting node for the search
        ParentNode = Node(Game.gameBoard,Game.gameBoard[y][x],startingCell,[[X==x and Y==y for X in range(boardSize)]for Y in range(boardSize)],None,(0,0),(x,y))

        # Adds all surrounding tiles neighbors) into the nodeQueue
        for neighbor in ParentNode.getNeighbors():
            nodeQueue.addTerm(ParentNode.makeChildNode(neighbor))

        # Finding words and prefixes from the nodeQueue
        while not nodeQueue.isEmpty():
            ParentNode = nodeQueue.removeTerm()
            # If current string is a word, add to list
            if ParentNode.checkWord() and ParentNode.currentWord not in wordsFound:
                wordNodes.append(ParentNode)
                wordsFound.add(ParentNode.currentWord)
                wordInstructions[ParentNode.currentWord] = ParentNode.getPath()
            # Adds neighboring node to nodeQueue if the string is a prefix of a word
            # and the neighboring node forms a prefix
            if ParentNode.checkPrefix():
                for neighbor in ParentNode.getNeighbors():
                    questionedChild = ParentNode.makeChildNode(neighbor)
                    if questionedChild.checkPrefix:
                        nodeQueue.addTerm(questionedChild)

# Print out Score, Words, and Steps
score = 0
# Prints the sorted list of found words based on length
print(sorted(wordsFound, key=len, reverse=True))
wordInstructionsSorted = {}
for item in sorted(wordInstructions, key=len, reverse=True):
    wordInstructionsSorted[item] = wordInstructions[item]
    score += calculateScore(item)


#Debug
#print(wordInstructionsSorted)
#print(f"the max score is: {score}")

#directions (1,1) moves one right and one down, (-1,1) moves one left and one down, (0,-1) moves one up.