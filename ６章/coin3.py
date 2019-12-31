def coincomparision(coinlist):
    counter = 0
    currlist = coinlist
    while len(currlist) > 1:
        group1, group2, group3 = splitcoin(currlist)
        currlist = findfake(group1, group2, group3)
    fake = currlist[0]

    print('The fake coin is coin', 
             coinlist.index(fake)+1,'in the original list')

    return 

def splitcoin(currlist):
    group1 = currlist[0:len(currlist)//3]
    group2 = currlist[len(currlist)//3:len(currlist)//3*2]
    group3 = currlist[len(currlist)//3*2:len(currlist)]

    return group1, group2, group3

def findfake(group1, group2, group3):
    result1and2 = compare(group1, group2)
    if result1and2 == 'left':
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeg = group1
        elif result1and3 == 'equal':
            fakeg = group1
    elif result1and2 == 'right':
        result2and3 = compare(group2, group3)
        if result2and3 == 'left':
            fakeg = group2
        elif result1and3 == 'equal':
            fakeg = group2
    elif result1and2 == 'equal':
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeg = group1
        elif result1and3 == 'right':
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
coinlist1 = [10, 10, 10, 10, 10, 10, 11, 11, 10]

coincomparision(coinlist1)