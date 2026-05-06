class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0 
        curr_consecutive = 0 
        for i in range(len(nums)):
            if nums[i] :
                curr_consecutive += 1
                if curr_consecutive > max_consecutive:
                    max_consecutive = curr_consecutive
            else:
                curr_consecutive = 0 

        return max_consecutive