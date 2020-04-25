# my favourite one <33333

def binary_search(array, value):
    first_index = 0
    last_index = len(array) - 1
    
    found = False

    while first_index <= last_index and not found:
        middle_index = (first_index + last_index)//2

        if array[middle_index] == value:
            found = True
    
        else:
            if value < array[middle_index]:
                last_index = middle_index - 1
                print("search in lower half")
            else:
                first_index = middle_index + 1
                print("search in upper half")

    return found

mylist = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(binary_search(mylist, 13))

