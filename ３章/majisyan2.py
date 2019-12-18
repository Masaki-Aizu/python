import itertools

# import numpy as np
# please check right of this code with input '777777'

# ls1 = [1, 2, 3]
# print(list(itertools.combinations(ls1, 2)))

deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']

# deck1 = np.array(deck)
# print(deck1.shape)

def ComputerAssistant():
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers, pairsuit = [], [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number' +
                               ' of at least 6 digits:'))

    # change
    ls = []
    i = 0
    while len(ls) < 5:
        number = number * (i + 1) // (i + 2)
        n = number % 52
        i += 1
        if n not in ls:
            ls.append(n)

    for i in range(5):
        n = ls[i]
        cards.append(deck[n])
        cind.append(n)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        # change
        if numsuits[n % 4] > 1:
            if n % 4 not in pairsuit:
              pairsuit.append(n % 4)
            
    # print (cards)
    # print(cnumbers)
    
    # change
    cardh = []
    for i in range(5):
        if cardsuits[i] in pairsuit:
            cardh.append([i, cardsuits[i]])
    
    print(cardh)
    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])

    sortList(remindices)
    outputNext3Cards(encode, remindices)

    guess = input('What is the hidden card?')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

def outputFirstCard(numbers, suits, cards):
    # change
    '''
    cnumbers = numbers: reserve a number of each cards
    oneTwo = cardh: reserve a list number and suit: [list number, suit]
    cards: reserve some input cards

    同じスートをもつカード同士でカードの差をとる
    そして、一番小さい差を持つものを隠しカードと見せるカードとする
    '''
    #change -------
    suits_tmp = []
    suits_tmp2 = []
    tmp = suits[0][1]
    for i in range(len(suits)):
        if suits[i][1] == tmp:
            suits_tmp.append(suits[i][0])
        else:
            suits_tmp2.append(suits[i][0])

    # print(suits_tmp)
    # print(suits_tmp2)
    
    true_encode = 14
    for oneTwo in list(itertools.combinations(suits_tmp, 2)):
        encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
        if encode > 0 and encode <= 6:
            if true_encode > encode:
                true_encode = encode
                hidden = oneTwo[0]
                other = oneTwo[1]
        else:
            if true_encode > encode:
                hidden = oneTwo[1]
                other = oneTwo[0]
                encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13
                true_encode = encode

    
    if len(suits_tmp2) != 0:
        for oneTwo in list(itertools.combinations(suits_tmp, 2)):
            encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
            if encode > 0 and encode <= 6:
                if true_encode > encode:
                    true_encode = encode
                    hidden = oneTwo[0]
                    other = oneTwo[1]
            else:
                if true_encode > encode:
                    hidden = oneTwo[1]
                    other = oneTwo[0]
                    encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13
    # ---------------
    
    '''
        else:
            hidden = oneTwo[1]
            other = oneTwo[0]
            encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13
    '''
    print ('First card is:', cards[other])

    return hidden, other, encode

def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return

def outputNext3Cards(code, ind):
    
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]       
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

ComputerAssistant()