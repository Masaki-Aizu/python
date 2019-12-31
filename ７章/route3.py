def serchforroot(x1, x2, epsilon):
    numg = 0
    low = x1
    high = x2
    n_x = (high + low) / 2.0
    while abs(n_x**3 + n_x**2 - 11) > epsilon:
        if (n_x**3 + n_x**2 - 11) > 0:
            high = n_x
        else:
            low = n_x
        n_x = (high + low) / 2
        numg += 1
    print('numGuesses = ', numg)
    print(n_x, 'is close to square root of x^3 + x^2 - 11')

    return

serchforroot(-10, 10, .01)