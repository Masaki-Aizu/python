def HowHardTheCrystal(n, d):
    r = 1
    while r ** d <= n:
        r += 1
    print('Radix chosen is ', r)
    num_d = 0
    d = checkd(n, d, r)
    nobreak = [0] * d
    for i in range(d):
        for j in range(r-1):
            nobreak[i] += 1
            Floor = converttodecimal(r, d, nobreak)
            if Floor > n:
                nobreak[i] -= 1
                break
            print('Drop ball', i+1, 'from Floor', Floor)
            yes = input('Did the ball break? (yes/no): ')
            num_d += 1
            if yes == 'yes':
                nobreak[i] -= 1
                break

    hardness = converttodecimal(r, d, nobreak)
    return hardness, num_d

def converttodecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r
    number += rep[d-1]

    return number

def checkd(n, d, r):
    count = 0
    crite = (r ** d)
    while crite > n:
        count += 1
        crite = crite / n
    
    if count > 0:
        print('use', d-count,'balls')
        
    return d - count

HowHardTheCrystal(128, 6)