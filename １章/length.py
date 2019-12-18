def press(ls):
    re_ls = []
    len_ls = []
    start = 0
    ls += ' '

    for i in range(1, len(ls)):
        if ls[i] != ls[start]:
            re_ls += [ls[start]]
            len_ls += [i - start]
            start = i
    
    # print(len_ls, re_ls)
    for i in range(len(len_ls)):
        print(len_ls[i], re_ls[i], sep='', end='')
    print()

    extend(len_ls, re_ls)

def extend(len_ls, re_ls):
    count = 0
    exten_ls = str()
    
    for i in len_ls:
        for j in range(i):
            exten_ls += re_ls[count]
        count += 1
    print(exten_ls)


ls = 'BWWWWWWBWWWW'
press(ls)