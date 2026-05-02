from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    # set_output = set()
    # for row_index, row in enumerate(grid):
    #     # print(f"row_index: {row_index} , row: {row}")
    #     for col_index, item in enumerate(row):
    #         if item == 1:
    #             set_output.add((row_index, col_index))
    # return set_output
    return {(r,c) for r,row in enumerate(grid) for c,item in enumerate(row) if item == 1}
# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
