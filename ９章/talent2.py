def hireshow(candls, candtal, talentls):
    newcandls, newtalentls = createcand(candls, candtal, talentls)
    #print(newcandls)
    #print(newtalentls)
    n = len(candls)
    hire = candls[:]
    #print(talentls)
    #print(candls)
    for i in range(2**n):
        num = i
        comb = []
        for j in range(n):
            if num % 2 == 1:
                comb = [candls[n-j-1]] + comb
            num = num // 2
        if goodcomb(comb, candls, candtal, talentls):
            if len(hire) > len(comb):
                #print(comb)
                #print(hire)
                hire = comb
    print('Optimum Solution: ', set(hire + newcandls))

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
    for i in range(len(candtal)):
        if check(i, candtal[i], candtal):
            for j in candtal[i]:
                # print(j)
                if j in talentls:
                    talentls.remove(j)
            newcand.append(candls[i])
            newtal.append(candtal[i])

    return newcand, newtal
               
def check(i, icand, candtal):
    n = len(icand)
    judge = [0] * n
    #print(judge)
    for j in range(n):
        for k in range(len(candtal)):
            if i == k:
                continue
            if icand[j] in candtal[k]:
                judge[j] += 1
    if 0 in judge:
        #print(judge)
        return True
    else:
        return False

Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalent5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList5 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CandToTalents5 = [ [1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9], [7, 8, 9], [1, 3, 5] ]

hireshow(Candidates, CandidateTalents, Talents)
hireshow(CandidateList5, CandToTalents5, ShowTalent5)