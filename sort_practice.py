def isort(a):
    for x in range(1, len(a)):
        b = a[x] # element present at index number 1
        c = x-1
        while c >=0 and b < a[c]: #comparing elements with the next until the last time
            a[c+1] = a[c]
            c -= 1      #comparing each element to the elements present to its left
        a[c+1] = b      #new item becomes the key



a = [24, 23, 534, 56, 1, 50, 17]
isort(a)
print(a)
