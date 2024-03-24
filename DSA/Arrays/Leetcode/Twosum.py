# nums = [2, 7, 11, 15]
# target = 9

# Indices of the two numbers whose sum is equal to the target:
# [0, 1]

# For the optimized version of the Two Sum problem, you could specify constraints such as optimizing the time complexity to O(n) using a hash table (dictionary in Python) for faster lookups. Let me know if you need an example of the optimized solution!

def two_sum(arr,target):
    dictionary= {}
    for index , num in enumerate(arr):
        complement = target - num
        if complement in dictionary:
            print([dictionary[complement],index])
        dictionary[num] = index
arr = [2, 7, 11, 15]
target = 9
two_sum(arr,target)