import math

# don't love this one

def jump_search(arr, val):
    step = 0
    found = False

    while step <= len(arr) - 1 and not found:
        if arr[step] == val:
            found = True
            return found, arr.index(val)
        else:
            step += int(math.sqrt(len(arr)))
            if step >= len(arr):
                step = len(arr) - 1
                break

        if arr[step] <= val:
            break

    step -= int(math.sqrt(len(arr)))

    while step <= len(arr) - 1 and not found:
        if arr[step] == val:
            found = True
            break
        step += 1

    else:
        return found

    return found, arr.index(val)

mylist = [1, 6, 8, 12, 15, 26, 32, 57, 91, 101, 123, 176, 188]
print(jump_search(mylist, 32))
