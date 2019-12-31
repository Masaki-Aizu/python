def bsearch(L, value, length):
    lo, hi = 0, len(L) - 1
    while (hi - lo) > length:
        mid = (lo + hi) // 2
        if L[mid] < value:
           lo = mid + 1
        elif value < L[mid]:
            hi = mid - 1
        else:
            return mid
        
    for i in range((hi - lo)+1):
        if L[i+lo] == value:
            return i+lo
    
    return 'NOTFOUND'


L = [1,2,3,4,5,6,7,8,9,10]
print(bsearch(L, 6, 3))
