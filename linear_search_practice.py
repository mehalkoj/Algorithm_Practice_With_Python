def search(mylist, z, key):
    # mylist = datalist, n = length of datalist, key = key,
    #this function is just for searching through a list for the element and returning it when its found
    for x in range(0, z):
        if (mylist[x] == key):
            return x
    return -1

# variables used above
mylist = [ 54, 2312, 22, 17, 5, 53, 4, 10, 11, 53, 65]
key = 17
z = len(mylist)

# This is all hear just for the printing of outcome
matched = search(mylist, z, key)
if(matched == -1):
    print('Key is not present')
else:
    print('Key is present in the given list at index', matched)
