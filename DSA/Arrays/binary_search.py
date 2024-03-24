## binary search
# Target 5 found at index 4.

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    mid = (left+right)//2
    if target == arr[mid]:
        print(mid)
    elif arr[mid] < target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid -1
    else :
        print("None")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
binary_search(arr,target)