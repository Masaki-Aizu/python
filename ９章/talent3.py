def hireshow(candls, candtal, talentls):
    n = len(candls)
    com = candls[:]
    hire = sum([i[1] for i in candls])
    # print(hire)
    for i in range(2**n):
        num = i
        comb = []
        for j in range(n):
            if num % 2 == 1:
                comb = [candls[n-j-1]] + comb
            num = num // 2
        if goodcomb(comb, candls, candtal, talentls):
            comb_sum = sum([k[1] for k in comb])
            #print(comb_sum)
            if hire > comb_sum:
                hire = comb_sum
                com = comb
                
    print('Optimum Solution: ', com)

def goodcomb(comb, candls, candtal, talentls):
    tmp_candls = [i[0] for i in candls]
    tmp_comb = [i[0] for i in comb]
    #print(tmp_candls)
    #print(tmp_comb)
    for tal in talentls:
        cover = False
        for cand in tmp_comb:
            ct = candtal[tmp_candls.index(cand)]
            #print(ct)
            #print(tal)
            if tal in ct:
                cover = True
        if not cover:
            return False
    return True

ShowTalent5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList5 = [('A', 3), ('B', 2), ('C', 1), ('D', 4), ('E', 5), ('F', 2), ('G', 7)]
CandToTalents5 = [ [1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9], [7, 8, 9], [1, 3, 5] ]

hireshow(CandidateList5, CandToTalents5, ShowTalent5)