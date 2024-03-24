# Linear Search



# Target 7 found at index 2.


def linear_search(arr,target):
    if not arr:
        return None
    for index in range(len(arr)):
        if target == arr[index]:
            founded_index = index
    print(founded_index)

arr = [4, 2, 7, 1, 9, 5]
target = 7
linear_search(arr,target)