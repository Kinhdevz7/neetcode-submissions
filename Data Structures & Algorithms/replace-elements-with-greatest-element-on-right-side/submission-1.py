class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force
        res = [0]*len(arr)
        for i in range(len(arr)):
            right_max = -1 
            for j in range(i+1,len(arr)):
                right_max = max(right_max, arr[j])
            res[i] = right_max 
        return  res