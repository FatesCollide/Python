class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        ans = []
        current = 0
        
        for num in nums:
            current += num
            ans.append(current)
        return ans
