def pleaseConformOnepass(caps):
    if len(caps) == 0:
        print('cap is empty!')
        return 
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        # print(i)
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                if len(caps)-2 == i:
                    print('Person at position ', i-1,' flip your cap!')
                    return
                print('Pople in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps!')

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'B']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = []

#pleaseConformOnepass(cap1)
#pleaseConformOnepass(cap2)
pleaseConformOnepass(cap3)