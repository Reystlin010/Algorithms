def find_smallest(nums: list) -> int:
    """Finds the smallest integer in a list and returns index"""
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i
    return smallest_index
        
def sort_select(nums: list) -> list:
    """Sorts the list from low to high"""
    sorted_list = []
    for i in range(len(nums)):
        smallest = find_smallest(nums)
        sorted_list.append(nums.pop(smallest))
    return sorted_list    




n = [1, 45, 3, 6]
print(sort_select(n))