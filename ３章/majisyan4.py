import itertools

deck = ['A_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '10_C', 'J_C', 'Q_C',
        'K_C', 'A_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'J_D', 'Q_D',
        'K_D','A_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H', 'J_H', 'Q_H',
        'K_H','A_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'J_S', 'Q_S',
        'K_S']

def ComputerAssistant():
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number' +
                               ' of at least 6 digits:'))

    # change
    ls = []
    i = 0
    while len(ls) < 4:
        number = number * (i + 1) // (i + 2)
        n = number % 52
        i += 1
        if n not in ls:
            ls.append(n)

    for i in range(4):
        n = ls[i]
        cards.append(deck[n])
        cind.append(n)
        '''
        cardsuits.append(n // 13)
        cnumbers.append(n % 13)

        numsuits[n // 13] += 1
        if numsuits[n // 13] > 1:
            pairsuit = n // 13
        '''    
    # print(cards)
    '''
    print(pairsuit)

    cardh = []
    for i in range(4):
        if cardsuits[i] == pairsuit:
            cardh.append(i)
    '''

    hidden, other, encode = hideFirstCard(cind, deck)

    '''
    remindices = []
    for i in range(4):
        if cind[i] != hidden:
            remindices.append(cind[i])
    '''

    # print(cind)

    cind = sortList(cind)

    # print(cind)
    
    remindices = []
    count = 0
    for i in range(4):
        if cind[i] != hidden:
            remindices.append(deck[cind[i]])
    
    for i in range(len(remindices)):
        if remindices[i] == deck[other]:
            count = i

    # print(remindices)
    # print(count)

    outputNext3Cards(encode, count, remindices)

    guess = input('What is the hidden card?')
    if guess == deck[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

def hideFirstCard(cind, deck):
    true_encode = 55
    # print(list(itertools.combinations(cind, 2)))
    for oneTwo in list(itertools.combinations(cind, 2)):
        encode = (cind[0] - cind[1]) % 52
        if encode > 0 and encode <= 13:
            if true_encode > encode:
                true_encode = encode
                hidden = oneTwo[0]
                other = oneTwo[1]
        else:
            if true_encode > encode:
                hidden = oneTwo[1]
                other = oneTwo[0]
                encode = (cind[1] - cind[0]) % 52
                true_encode = encode
    
    # print(hidden, other)

    return hidden, other, true_encode

def sortList(tlist):
    small_ls = []
    for i in range(len(tlist)):
        small_ls.append(tlist.pop(selectionsort(tlist)))
    
    return small_ls

def selectionsort(tlist):
    smallest = tlist[0]
    smallest_index = 0

    for j in range(1, len(tlist)):
        if smallest > tlist[j]:
            smallest = tlist[j]
            smallest_index = j
    
    return smallest_index

def outputNext3Cards(code, count, ind):
    tmp = bin(code)
    # print(tmp)
    # print(tmp[len(tmp)-1])
    num = 0
    for i in range(1, 4):
        if tmp[len(tmp)-i] == '1':
            print ('put right side')
        elif tmp[len(tmp)-i] == '0':
            print ('put left side')
        if num == count:
            print(ind[count]) # 基点となるカードを表にしておく
        num += 1

    if tmp[len(tmp)-5] == '1':
        print ('reverse all card')
    else:
        print ('not reverse the cards')

ComputerAssistant()