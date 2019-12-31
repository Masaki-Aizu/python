import random as rd
import copy

def coincomparision(coinlist):
    counter = 0
    currlist = coinlist
    checklist = copy.deepcopy(coinlist)
    while len(currlist) > 1:
        group1, group2, group3 = splitcoin(currlist)
        currlist = findfake(group1, group2, group3)
        counter += 1
    fake = currlist[0]
    checklist.remove(fake)
    
    # print(coinlist)
    # print(currlist)
    # print(checklist)
   
    if fake == checklist[rd.randint(0, len(checklist))]:
        print('The fake coin is not here')
        return 

    print('The fake coin is coin', 
             coinlist.index(fake)+1,'in the original list')

    print('Number of weights: ', counter)

    return 

def splitcoin(currlist):
    group1 = currlist[0:len(currlist)//3]
    group2 = currlist[len(currlist)//3:len(currlist)//3*2]
    group3 = currlist[len(currlist)//3*2:len(currlist)]

    return group1, group2, group3

def findfake(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeg = group1
    elif result1and2 == 'right':
        fakeg = group2
    elif result1and2 == 'equal':
        fakeg = group3

    return fakeg

def compare(group1, group2):
    if sum(group1) > sum(group2):
        result = 'left'
    elif sum(group1) < sum(group2):
        result = 'right'
    elif sum(group1) == sum(group2):
        result = 'equal'

    return result

coinlist = [10, 10, 10, 10, 10, 10, 10, 10, 10]
coinlist1 = [10, 11, 10, 10, 10, 10, 10, 10, 10]

coincomparision(coinlist)

