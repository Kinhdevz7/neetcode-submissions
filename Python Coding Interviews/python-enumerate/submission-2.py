from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, curr_number in enumerate(nums):
        if curr_number != 7:
            continue
        else:
            return i 
    return -1 


def get_dist_between_sevens(nums: List[int]) -> int:
    first_occ = None
    second_occ = None
    for index, curr_number in enumerate(nums):
        if curr_number != 7:
            continue
        elif first_occ is None :
            first_occ = index 
        elif second_occ is None:
            second_occ = index
        else :
            return abs(first_occ - second_occ)
    return 

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
