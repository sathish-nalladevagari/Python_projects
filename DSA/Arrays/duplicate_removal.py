
    # Array after duplicate removal: [1, 2, 3, 4, 5]

# it is by changing its type to set and list


# def duplicate_removal(arr):
#     arr = set(arr)
#     print(list(arr))
# arr = [1, 2, 3, 2, 4, 5, 3]
# duplicate_removal(arr)

# using temperory space


def duplicate_removal(arr):
    temp = []
    if not arr:
        return None
    for num in arr:
        if num not in temp:
            temp.append(num)
    print(temp)
     
arr = [1, 2, 3, 2, 4, 5, 3]

duplicate_removal(arr)