def linear_search_ordered(array, value):
    index = 0
    found = False
    stopped = False

    while index < len(array) and not found and not stopped:
        if array[index] == value:
            found = True
        else:
            if value < array[index]:
                stopped = True
            else:
                index += 1
    return found, index

mylist = [2,3,4,5,6,7,8,9]

found, index = linear_search_ordered(mylist, 4)

print(found)
print(index)