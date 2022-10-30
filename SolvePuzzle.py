from array import ArrayType
import random
from tokenize import Number
import numpy as np

from PuzzleNode import PuzzleNode


class SolvePuzzle:
    def __init__(self, size:Number,):
        self.puzzleSize = size
        self.openQueue = []
        self.closedQueue = []

    def initPuzzle(self):  
        temp_array = np.arange(self.puzzleSize * self.puzzleSize)
        random.shuffle(temp_array)
        puzzle =temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return puzzle
    
    def initGoalPuzzle(self):
        temp_array = np.arange(self.puzzleSize * self.puzzleSize)
        #     random.shuffle(temp_array)
        goal = temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return goal

    def get_fValue(self, startNode:PuzzleNode, goal):
        # calculate Heuristic value f(x) = h(x) + g(x)
        return self.getHeuristicValue(startNode.puzzle, goal) + startNode.depth_g

    def getHeuristicValue(self, currentPuz, goalPuz):
        # Calculates the number  of miisplaced tiles between the given puzzles
        count = 0
        for row in range(0, self.puzzleSize):
            for col in range(0, self.puzzleSize):
                if currentPuz[row][col] != goalPuz[row][col] and currentPuz[row][col] != 0:
                    count += 1
        return count
    

    def solvePuzzle(self):
        num = 9
        startPuz = self.initPuzzle()
        goalPuz = self.initGoalPuzzle()
        startNode = PuzzleNode(startPuz, 0, 0)
        startNode.f_score = self.get_fValue(startNode, goalPuz)
        # add the startNode in the open Queue
        self.openQueue.append(startNode)
        # print("\n\n")
        while num > 0:
            currentNode:PuzzleNode = self.openQueue[0]
            print("==================================================\n")
        #     for i in cur.data:
        #         for j in i:
        #             print(j, end=" ")
        #         print("")
            # if there is no difference between currentNode puzzle and goal node 
            # we have solved the puzzle
            if (self.getHeuristicValue(currentNode.puzzle, goalPuz) == 0):
                break
            for node in currentNode.expandCurrentNode():
                # print(node.puzzle, "<<<node \n\n")
                node.f_score = self.get_fValue(node, goalPuz)
                self.openQueue.append(node)
            self.closedQueue.append(currentNode)
            print(self.openQueue, "before \n\n")
            del self.openQueue[0]
            print(self.openQueue, "after \n\n")
            # # sort the open list based on f value
            # self.open.sort(key=lambda x: x.fval, reverse=False
            num -= 1

puz = SolvePuzzle(3)
puz.solvePuzzle()