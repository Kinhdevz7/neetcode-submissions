class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        res = [-1]*N
        # Base case when arr is empty or 1
        if not N or N == 1:
            return res

        right_max = arr[-1]
        # print(f"initial right_max: {right_max}")
        for i in range(N-2, -1, -1):
            res[i] = right_max
            # print(f"i: {i}")
            # print(f"res: {res}")
            right_max = max(right_max, arr[i])
            # print(f"right_max: {right_max}")

        return res