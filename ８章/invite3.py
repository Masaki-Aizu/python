def invitelist(guestls, dislikels):
    n, invite = len(guestls), []
    opt_wei = 0
    for i in range(2**n):
        comb = []
        tmp_com = []
        num = i
        weight = 0
        flag = 0
        for j in range(n):
            if num % 2 == 1:
                comb = [guestls[n-j-1]] + comb
                tmp_com = [guestls[n-j-1][0]] + tmp_com   
            num = num // 2
        good = True
        for j in dislikels:
            if j[0] in tmp_com and j[1] in tmp_com:
                flag += 1
        if flag > 1:
            good = False
        if good:
            # print(tmp_com)
            for j in comb:
                weight += j[1]
            if weight > opt_wei:
                invite = comb
                opt_wei = weight
    
    print('Optimum sollution:', invite)
    return 

dislikepairs = [['B', 'C'],['C', 'D'], ['D', 'E'], ['F', 'G'], 
                  ['F', 'H'], ['F', 'I'], ['G', 'H']]
guestlist = [('A', 2), ('B', 1), ('C', 3), ('D', 2), 
                   ('E', 1), ('F', 4), ('G', 2), ('H', 1), ('I', 3)]
# dislikepairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
# guestlist = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
invitelist(guestlist, dislikepairs)