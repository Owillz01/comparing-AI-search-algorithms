#https://www.researchgate.net/figure/8-Puzzle-problem-instances_tbl1_280545587
# https://stackoverflow.com/questions/60747903/n-puzzle-problem-using-a-star-search-algorithm
statesList = [
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [1,3,4,8,6,2,7,0,5],
        "steps": 5
    },
    {
        "start" : [0,3,5,4,2,8,6,1,7],
        "goal" : [0,1,2,3,4,5,6,7,8],
        "steps": 10
    },
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [2,8,1,4,6,3,0,7,5],
        "steps": 12
    },
    {
        "start" : [2,3,1,7,0,8,6,5,4],
        "goal" : [1,2,3,8,0,4,7,6,5],
        "steps": 14
    }, 
    {
        "start" : [2,3,1,8,0,4,7,6,5],
        "goal" : [1,2,3,8,0,4,7,6,5],
        "steps": 16
    },
    {
        "start" : [1,2,3,8,0,4,7,6,5],
        "goal" : [2,3,1,8,0,4,7,6,5],
        "steps": 16
    },
]
def getstateInstance(index):
    if index < 6:
        return statesList[index]


def getAllInstance():
    return statesList