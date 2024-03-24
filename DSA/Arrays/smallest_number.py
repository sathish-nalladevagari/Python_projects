
## smallest number


def smallest_number(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    print(smallest)



arr = [5, 12, 3, 8, 10, 1, 6]

smallest_number(arr)