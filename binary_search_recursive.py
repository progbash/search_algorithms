def binary_search_recursive(array, value):
    if len(array) == 0:
        return False
    else:
        middle_index = len(array)//2
        
        if array[middle_index] == value:
            return True
        
        else:
            if value < array[middle_index]:
                return binary_search_recursive(array[:middle_index], value), array.index(value)
            else:
                return binary_search_recursive(array[middle_index+1:], value), array.index(value)

mylist = [3,6,9,12,15,17,21]
print(binary_search_recursive(mylist, 17))