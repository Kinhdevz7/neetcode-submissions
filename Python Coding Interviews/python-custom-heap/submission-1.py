import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    out = []
    for num in nums:
        heapq.heappush(max_heap, (-num, num))
    while max_heap:
        a_tuple = heapq.heappop(max_heap)
        original_num = a_tuple[1]
        out.append(original_num)
    return out




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
