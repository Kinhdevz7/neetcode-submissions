from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(key = lambda x : len(x), reverse= True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = lambda x: abs(x))
    return numbers

def sum_3_integers(triplet:List[int]) -> int:
    x,y,z = triplet
    return x+y+z 

def compute_volume(box_dimensions: Tuple[int,int,int]) -> int:
    width, height, depth = box_dimensions
    return width*height*depth


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
