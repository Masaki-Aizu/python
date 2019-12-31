def serchforroot(x, epsilon):
    if x < 0:
        print('Sorry, Imaginally numbers iare out of scope')
        return 

    if x <= 1:
        numg = 0
        low = 0.0
        high = 1
        ans = (high + low) / 2.0
    else:
        numg = 0
        low = 0.0
        high = x
        ans = (high + low) / 2.0
    while abs(ans**2 - x) > epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high +low) / 2
        numg += 1
    print('numGuesses = ', numg)
    print(ans, 'is close to square root of', x)

    return

serchforroot(1, .01)
