from array import ArrayType
from time import time
from tokenize import Number
import numpy as np
# from DrawBoard import DrawBoard

from PuzzleNode import PuzzleNode

import State as pz



class SolvePuzzle:
    def __init__(self, index:Number,):
        self.puzzleSize = 3
        self.puzzleInstance = pz.getstateInstance(index)
        self.openQueue = []
        self.closedQueue = []

    def initPuzzle(self):  
        temp_array = np.array(self.puzzleInstance['start'])
        puzzle = temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return puzzle
    
    def initGoalPuzzle(self):
        temp_array = np.array(self.puzzleInstance['goal'])
        goal = temp_array.reshape(self.puzzleSize,self.puzzleSize)
        return goal

    def get_fValue(self, currentNode:PuzzleNode, goal, title):
        # calculate Heuristic value f(x) = h(x) + g(x) or f(x) = h(x) for greedy best search
        if title == "Greedy":
            return self.getHeuristicValue(currentNode.puzzle, goal)
        else:
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
        return lambda nodesList:nodesList.f_score
    
    def preventRevisitingOfNode(self, child, parentNode:PuzzleNode):
        isFound = True
        # if len(parentNode.closedQueue) > 0:
        #     # .all() compares all the elements of the array and only return true if they all exist
        #     if (child.puzzle == parentNode.closedQueue[-1].puzzle).all():
        #         print("it exist!!!")
        #         isFound = True
        # return isFound
        if child not in  parentNode.closedQueue:
            # print("it exist!!!")
            isFound = False
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


    def solvePuzzleA_star(self):
        startPuz = self.initPuzzle()
        a_star = {
            "solution":"",
            "opened": "",
            "time":"",
            "status":""
        }
        if self.isPuzsolvable(startPuz):
            goalPuz = self.initGoalPuzzle()
            time1 = time()
            aStar =  self.solve(startPuz, goalPuz, "a*")
            aStarTime = time() - time1
            a_star['solution'] = aStar[0]
            a_star['opened'] = aStar[1]
            a_star['time']= str(aStarTime)
            a_star['status']= aStar[2]
        return a_star
    

    def solvePuzzleGreedy(self):
        startPuz = self.initPuzzle()
        greedy = {
            "solution":"",
            "opened": "",
            "time":"",
            "status":""
        }
        if self.isPuzsolvable(startPuz):
            goalPuz = self.initGoalPuzzle()
            current_time = time()
            greedyBS =  self.solve(startPuz, goalPuz, "Greedy")
            greedyBSTime = time() - current_time
            greedy['solution'] = greedyBS[0]
            greedy['opened'] = greedyBS[1]
            greedy['time'] = str(greedyBSTime)
            greedy['status']= greedyBS[2]
        return greedy
    



    def solve(self, startPuz, goalPuz, title):

        parentNode = PuzzleNode(startPuz, 0, 0)
        parentNode.f_score = self.get_fValue(parentNode, goalPuz, title)
        print("len(parentNode.closedQueue) start!!!", len(parentNode.closedQueue))
        # add the startNode in the open Queue
        parentNode.openQueue.append(parentNode)
        timeOut = time() + 60
        while True:
            node:PuzzleNode = parentNode.openQueue[0]
            print(f"=== {title} TIME: {time()+60 - timeOut} CURRENT DEPTH LEVEL================> {len(parentNode.closedQueue)}  <=======\n")
            # if there is no difference between currentNode puzzle and goal puzzle
            # we have solved the puzzle
            if (self.getHeuristicValue(node.puzzle, goalPuz) == 0):
                print("Solved!!!", parentNode.depth_g)
                return (node.puzzle, len(parentNode.closedQueue), "Solved!")
            if (time() > timeOut):
                print("STOPPED!!!", parentNode.depth_g)
                return (node.puzzle, len(parentNode.closedQueue), "Not Solved!")
            else:
                childrenNodes = node.expandCurrentNode()
                for childNode in childrenNodes:
                    arrayExist = self.preventRevisitingOfNode(childNode, parentNode)
                    if not arrayExist:
                        childNode.f_score = self.get_fValue(childNode, goalPuz, title)
                        parentNode.openQueue.append(childNode)
            # print(len(parentNode.closedQueue), "parentNode.closedQueue length")
            parentNode.closedQueue.add(node)
            del parentNode.openQueue[0]
            # sort the openQueue array based on the value of f_score
            parentNode.openQueue.sort(key=lambda nodesList:nodesList.f_score, reverse=False)

    
    
    # def greedy(self, startPuz, goalPuz):

    #     parentNode = PuzzleNode(startPuz, 0, 0)
    #     parentNode.f_score = self.getHeuristicValue(parentNode.puzzle, goalPuz)

    #     # add the startNode in the open Queue
    #     parentNode.openQueue.append(parentNode)
    #     while True:
    #         node:PuzzleNode = parentNode.openQueue[0]
    #         print("==================================================\n")
    #         # if there is no difference between currentNode puzzle and goal puzzle
    #         # we have solved the puzzle
    #         if (self.getHeuristicValue(node.puzzle, goalPuz) == 0):
    #             print("Puzzle Solved!!!")
    #             return (node.puzzle, len(parentNode.closedQueue))
    #         else:
    #             childrenNodes = node.expandCurrentNode()
    #             for childNode in childrenNodes:
    #                 arrayExist = self.preventRevisitingOfNode(childNode, parentNode)
    #                 if not arrayExist:
    #                     childNode.f_score = self.getHeuristicValue(childNode.puzzle, goalPuz)
    #                     parentNode.openQueue.append(childNode)
    #         # print(len(parentNode.closedQueue), "parentNode.closedQueue length")
    #         parentNode.closedQueue.add(node)
    #         del parentNode.openQueue[0]
    #         # sort the openQueue array based on the value of f_score
    #         parentNode.openQueue.sort(key=self.sortOpenQueueNodes)


    # puz = SolvePuzzle(2)  
    # puz.solvePuzzleGreedy() 