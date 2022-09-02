def bin_search(a, key):
    l = 0
    r = len(a)-1
    matched = False
    while( l<=r and not matched):
        middle = (l + r)//2
        if a[middle] == key:
            matched = True
        else:
            if key < a[middle]:
                r = middle - 1
            else:
                l = middle + 1
    return matched
print(bin_search([2, 3, 56, 13, 1], 56))
print(bin_search([2, 3, 56, 13, 1], 26))
print(bin_search(['James', 'Willim', 'Cat', 'Dan', 'Brian'], 'Dan'))