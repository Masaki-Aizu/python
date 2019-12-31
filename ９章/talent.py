def hireshow(candls, candtal, talentls):
    newcandls, newtalentls = createcand(candls, candtal, talentls)
    n = len(newcandls)
    hire = newcandls[:]
    for i in range(2**n):
        num = i
        comb = []
        for j in range(n):
            if num % 2 == 1:
                comb = [newcandls[n-j-1]] + comb
            num = num // 2
        if goodcomb(comb, newcandls, newtalentls, talentls):
            if len(hire) > len(comb):
                hire = comb
    print('Optimum Solution: ', hire)

def goodcomb(comb, candls, candtal, talentls):
    for tal in talentls:
        cover = False
        for cand in comb:
            ct = candtal[candls.index(cand)]
            if tal in ct:
                cover = True
        if not cover:
            return False
    return True

def createcand(candls, candtal, talentls):
    newcand = []
    newtal = []
    for i in range(len(candls)):
        contain = False
        for j in range(len(candls)):
            if i == j:
                continue
            if check(candtal[i], candtal[j]):
                contain = True
        if not contain:
            newcand.append(candls[i])
            newtal.append(candtal[i])

    return newcand, newtal

def check(icand, jcand):
    for i in icand:
        if i not in jcand:
            return False
    return True
               

Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

hireshow(Candidates, CandidateTalents, Talents)