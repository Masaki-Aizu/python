def invitelist(guestls, dislikels):
    dislike = []
    for i in dislikepairs:
        if i[0] in guestls:
            dislike.append(guestls.pop(guestls.index(i[0])))
        if i[1] in guestls:
            dislike.append(guestls.pop(guestls.index(i[1])))
    n, invite = len(dislike), []
    print(dislike)
    # print(guestlist)
    for i in range(2**n):
        comb = []
        num = i
        for j in range(n):
            if num % 2 == 1:
                comb = [dislike[n-j-1]] + comb  
            num = num // 2
        good = True
        for j in dislikels:
            if j[0] in comb and j[1] in comb:
                good = False
        if good:
            if len(comb) > len(invite):
                invite = comb
    invite.extend(guestls)
    print('Optimum sollution:', invite)
    return 

dislikepairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
guestlist = ['Alice', 'Bob', 'Cleo', 'Don', 'Eve']
invitelist(guestlist, dislikepairs)