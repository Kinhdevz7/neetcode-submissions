class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [-1] * 2*N
        print(ans)
        for i in range(N):
            ans[i] = nums[i]
            ans[i+N] = nums[i]
        print(ans)
        return ans
