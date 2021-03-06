def invitelist(guestls, dislikels):
    n, invite = len(guestls), []
    opt_wei = 0
    for i in range(2**n):
        comb = []
        tmp_com = []
        num = i
        weight = 0
        for j in range(n):
            if num % 2 == 1:
                comb = [guestls[n-j-1]] + comb
                tmp_com = [guestls[n-j-1][0]] + tmp_com   
            num = num // 2
        good = True
        for j in dislikels:
            if j[0] in tmp_com and j[1] in tmp_com:
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

dislikepairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
guestlist = [('Alice', 2), ('Bob', 6), ('Cleo', 3), ('Don', 10), ('Eve', 3)]
invitelist(guestlist, dislikepairs)
