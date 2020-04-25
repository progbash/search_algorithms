def linear_search_unordered(array, value):
    index = 0
    found = False

    while index < len(array) and not found:
        if array[index] == value:
            found = True
        else:
            index += 1
    return found, index

mylist = [4,5,7,2,8,2,3]

found, index = linear_search_unordered(mylist, 8)

print(found)
print(index)