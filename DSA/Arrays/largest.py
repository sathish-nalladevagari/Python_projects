# Largest among N numbers in an array

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for i in numbers[1:]:
        if i > largest:
            largest = i
    print(largest)

    

numbers = [23, 56, 78, 12, 45, 67, 89]

find_largest(numbers)