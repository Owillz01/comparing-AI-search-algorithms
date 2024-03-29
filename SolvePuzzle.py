from array import ArrayType
from time import time
from tokenize import Number
import numpy as np
from DrawBoard import DrawBoard

from PuzzleNode import PuzzleNode

import State as pz



class SolvePuzzle:
    def __init__(self, index:Number,):
        self.puzzleSize = 3
        self.puzzleInstance = pz.getstateInstance(index)
        # self.openQueue = []
        # self.closedQueue = []

    def initPuzzle(self):  
        temp_array = np.array(self.puzzleInstance['start'])
        puzzle = temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return puzzle
    
    def initGoalPuzzle(self):
        temp_array = np.array(self.puzzleInstance['goal'])
        goal = temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return goal

    def get_fValue(self, currentNode:PuzzleNode, goal):
        # calculate Heuristic value f(x) = h(x) + g(x)
        return self.getHeuristicValue(currentNode.puzzle, goal) + currentNode.depth_g

    def getHeuristicValue(self, currentPuz, goalPuz):
        # Calculates the number  of misplaced tiles between the given puzzles
        count = 0
        for row in range(0, self.puzzleSize):
            for col in range(0, self.puzzleSize):
                if currentPuz[row][col] != goalPuz[row][col] and currentPuz[row][col] != 0:
                    count += 1
        return count

    def sortOpenQueueNodes(self, nodesList:PuzzleNode):
        return nodesList.f_score
    
    def preventRevisitingOfNode(self, child, parentNode:PuzzleNode):
        isFound = False
        if len(parentNode.closedQueue) > 0:
            # .all() compares all the elements of the array and only return true if they all exist
            if (child.puzzle == parentNode.closedQueue[-1].puzzle).all():
                print("it exist!!!")
                isFound = True
        return isFound
            
    #count the number of inversions       
    def getInvertionCount(self, puzzle):
        inv = 0
        for i in range(len(puzzle)-1):
            for j in range(i+1 , len(puzzle)):
                if (( puzzle[i] > puzzle[j]).all() and puzzle[i] and puzzle[j]):
                    inv += 1
        return inv

    # check if the initial state of the puzzle is solvable
    def isPuzsolvable(self, puzzle): 
        inv_counter = self.getInvertionCount(puzzle)
        if (inv_counter %2 == 0):
            return True
        return False

    def solvePuzzle(self):
        startPuz = self.initPuzzle()
        a_star = {
            "solution":"ffffff",
            "opened": "",
            "time":""
        }
        greedy = {
            "solution":"",
            "opened": "",
            "time":""
        }
        if self.isPuzsolvable(startPuz):
            goalPuz = self.initGoalPuzzle()
            # DrawBoard(self.puzzleSize, startPuz)
            
            time1 = time()
            aStar =  self.a_star(startPuz, goalPuz)
            aStarTime = time() - time1
            a_star['solution'] = aStar[0]
            a_star['opened'] = aStar[1]
            a_star['time']= aStarTime
            # print('A* Solution is ', aStar[0])
            # print('Number of A* opened nodes is ', aStar[1])
            # print('A* Time:', aStarTime, "\n") 

            time2 = time()
            greedyBS =  self.greedy(startPuz, goalPuz)
            greedyBSTime = time() - time2
            greedy['solution'] = greedyBS[0]
            greedy['opened'] = greedyBS[1]
            greedy['time'] = greedyBSTime
            # print('Gredy BS Solution is ', greedyBS[0])
            # print('Number of greedy BS opened nodes is ', greedyBS[1])
            # print('greedy BS Time:', greedyBSTime, "\n")  
        return (a_star, greedy)
    



    def a_star(self, startPuz, goalPuz):

        parentNode = PuzzleNode(startPuz, 0, 0)
        parentNode.f_score = self.get_fValue(parentNode, goalPuz)

        # add the startNode in the open Queue
        parentNode.openQueue.append(parentNode)
        while True:
            node:PuzzleNode = parentNode.openQueue[0]
            print("==================================================\n")
            # if there is no difference between currentNode puzzle and goal puzzle
            # we have solved the puzzle
            if (self.getHeuristicValue(node.puzzle, goalPuz) == 0):
                print("Puzzle Solved!!!")
                return (node.puzzle, len(parentNode.closedQueue))
            else:
                childrenNodes = node.expandCurrentNode()
                for childNode in childrenNodes:
                    arrayExist = self.preventRevisitingOfNode(childNode, parentNode)
                    if not arrayExist:
                        childNode.f_score = self.get_fValue(childNode, goalPuz)
                        parentNode.openQueue.append(childNode)
            # print(len(parentNode.closedQueue), "parentNode.closedQueue length")
            parentNode.closedQueue.append(node)
            del parentNode.openQueue[0]
            # sort the openQueue array based on the value of f_score
            parentNode.openQueue.sort(key=self.sortOpenQueueNodes)

    def greedy(self, startPuz, goalPuz):

        parentNode = PuzzleNode(startPuz, 0, 0)
        parentNode.f_score = self.getHeuristicValue(parentNode.puzzle, goalPuz)

        # add the startNode in the open Queue
        parentNode.openQueue.append(parentNode)
        while True:
            node:PuzzleNode = parentNode.openQueue[0]
            print("==================================================\n")
            # if there is no difference between currentNode puzzle and goal puzzle
            # we have solved the puzzle
            if (self.getHeuristicValue(node.puzzle, goalPuz) == 0):
                print("Puzzle Solved!!!")
                return (node.puzzle, len(parentNode.closedQueue))
            else:
                childrenNodes = node.expandCurrentNode()
                for childNode in childrenNodes:
                    arrayExist = self.preventRevisitingOfNode(childNode, parentNode)
                    if not arrayExist:
                        childNode.f_score = self.getHeuristicValue(childNode.puzzle, goalPuz)
                        parentNode.openQueue.append(childNode)
            # print(len(parentNode.closedQueue), "parentNode.closedQueue length")
            parentNode.closedQueue.append(node)
            del parentNode.openQueue[0]
            # sort the openQueue array based on the value of f_score
            parentNode.openQueue.sort(key=self.sortOpenQueueNodes)

