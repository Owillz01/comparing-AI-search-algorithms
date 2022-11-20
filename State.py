#https://www.researchgate.net/figure/8-Puzzle-problem-instances_tbl1_280545587

statesList = [
    {
        "start" : [2,8,3,1,0,4,7,6,5],
        "goal" : [1,2,3,8,0,4,7,6,5]
    },
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [1,3,4,8,6,2,7,0,5]
    },
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [2,8,1,4,6,3,0,7,5]
    },
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [5,6,7,4,0,8,3,2,1]
    },
    {
        "start" : [8,6,7,2,5,4,3,0,1],
        "goal" : [1,2,3,4,5,6,7,8,0]
    }, 
    {
        "start" : [6,4,7,8,5,0,3,2,1],
        "goal" : [1,2,3,4,5,6,7,8,0]
    },
]
def getstateInstance(index):
    return statesList[index]

