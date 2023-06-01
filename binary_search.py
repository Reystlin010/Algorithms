array_of_numbers = [1, 3, 4, 5, 6, 7]

def binary_search(numbers_list: list, item: int) -> int:
    """Finds guessed number in an array"""
    low = 0
    high = len(numbers_list) - 1

    while low <= high:    
        mid = round((low + high) / 2)
        guess = numbers_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
        
print(binary_search(array_of_numbers, 7))
        