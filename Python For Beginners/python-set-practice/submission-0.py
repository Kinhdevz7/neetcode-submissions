from typing import List

def contains_duplicate(words: List[str]) -> bool:
    length_list = len(words)
    my_set = set(words)
    length_set = len(my_set)
    if length_set < length_list:
        return True
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
