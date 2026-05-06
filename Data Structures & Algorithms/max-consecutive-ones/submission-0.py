class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = cnt = 0
        for num in nums:
            if num: 
                cnt += 1 
            else:
                max_cnt = max(cnt, max_cnt)
                cnt = 0 
                
        max_cnt = max(cnt, max_cnt)
        return max_cnt 