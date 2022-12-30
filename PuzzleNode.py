class PuzzleNode:
    openQueue = []
    # closedQueue = []
    closedQueue = set()
    # f = open("puzzleTrack.txt", "a")
    def __init__(self, _puzzle, _depth_g, _f_score):
        self.puzzle = _puzzle
        self.depth_g = _depth_g
        self.f_score = _f_score
    
    def getPositionOfIntZero(self):
        # it gets the row and column index of number 0 in the puzzle
        for row in range(0, len(self.puzzle)):
            for col in range(0, len(self.puzzle)):
                if self.puzzle[row][col] == 0:
                    return row, col

    def duplicateNodePuzzle(self,puzzle):
        temp_puzzle = []
        for i in puzzle:
            rows = []
            for j in i:
                rows.append(j)
            temp_puzzle.append(rows)
        return temp_puzzle


    def moveTiles(self, zeroRowIndex, zeroColIndex, newRowIndex, newColIndex):
        #  check that the new position index provided is not outside the env
        #  if it is outside the env return None else move the tile
        if newRowIndex >= 0 and newRowIndex < len(self.puzzle) and newColIndex >= 0 and newColIndex < len(self.puzzle):
            dupPuzzle = []
            dupPuzzle = self.duplicateNodePuzzle(self.puzzle)
            # get the current value of 0's new position
            currentValue = dupPuzzle[newRowIndex][newColIndex]  
            # swap positions for both tiles   
            dupPuzzle[newRowIndex][newColIndex] = dupPuzzle[zeroRowIndex][zeroColIndex]
            dupPuzzle[zeroRowIndex][zeroColIndex] = currentValue
            return dupPuzzle
        else:
            return None
    
    def expandCurrentNode(self):
        # expands the current node and return all possible movements {up,down,left,right} array/nodes
        # from the current position of 0 where

        # UP = [x-1, y], RIGHT = [x, y+1], DOWN = [x+1, y], LEFT = [x, y-1], 

        row, col = self.getPositionOfIntZero()
        possibleDirections = [[row - 1, col], [row, col + 1], [row + 1, col], [row, col - 1]]
        children = []
        for direction in possibleDirections:
            child = self.moveTiles(row, col, direction[0], direction[1])
            if child is not None:
                child_node = PuzzleNode(child, self.depth_g + 1, 0)
                children.append(child_node)
        return children
