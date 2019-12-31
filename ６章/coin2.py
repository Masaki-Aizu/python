import random as rd
import copy

def coincomparision(coinlist):
    counter = 0
    currlist = coinlist
    checklist = copy.deepcopy(coinlist)
    
    group1, group2, group3 = splitcoin(currlist)
    currlist, ctype = findfaketype(group1, group2, group3)
    counter += 2

    if currlist == 1:
        print('The fake coin is not here')
        return 

    print('coin type is ', ctype)

    while len(currlist) > 1:
        group1, group2, group3 = splitcoin(currlist)
        if ctype == 'heavier':
            currlist = findheavy(group1, group2, group3)
        elif ctype == 'lighter':
            currlist = findlight(group1, group2, group3)
        counter += 1
    fake = currlist[0]

    print('The fake coin is coin', 
             coinlist.index(fake)+1,'in the original list')

    print('Number of weights: ', counter)

    return 

def splitcoin(currlist):
    group1 = currlist[0:len(currlist)//3]
    group2 = currlist[len(currlist)//3:len(currlist)//3*2]
    group3 = currlist[len(currlist)//3*2:len(currlist)]

    return group1, group2, group3

def findfaketype(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeg = group1
            ctype = 'heavier'
        elif result1and3 == 'equal':
            fakeg = group2
            ctype = 'lighter'
    elif result1and2 == 'right':
        result2and3 = compare(group2, group3)
        if result2and3 == 'left':
            fakeg = group2
            ctype = 'heavier'
        elif result2and3 == 'equal':
            fakeg = group1
            ctype = 'lighter'
    elif result1and2 == 'equal':
        result1and3 = compare(group1, group3)
        if result1and3 == 'right':
            fakeg = group3
            ctype = 'heavier'
        elif result1and3 == 'left':
            fakeg = group3
            ctype = 'lighter'
        else:
            fakeg = 1
            ctype = 1

    return fakeg, ctype

def compare(group1, group2):
    if sum(group1) > sum(group2):
        result = 'left'
    elif sum(group1) < sum(group2):
        result = 'right'
    elif sum(group1) == sum(group2):
        result = 'equal'

    return result

def findheavy(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeg = group1
    elif result1and2 == 'right':
        fakeg = group2
    elif result1and2 == 'equal':
        fakeg = group3

    return fakeg

def findlight(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        fakeg = group2
    elif result1and2 == 'right':
        fakeg = group1
    elif result1and2 == 'equal':
        fakeg = group3

    return fakeg


coinlist = [10, 10, 10, 10, 10, 10, 10, 10, 10]
coinlist1 = [10, 11, 10, 10, 10, 10, 10, 10, 10]
coinlist2 = [10, 10, 9, 10, 10, 10, 10, 10, 10]

coincomparision(coinlist2)