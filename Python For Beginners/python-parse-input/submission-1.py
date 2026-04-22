from typing import List

def read_integers() -> List[int]:
    user_input = input()
    int_list = user_input.split(",")
    return int_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
