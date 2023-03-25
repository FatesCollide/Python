class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        index = 0
        for num in nums:
        
            if target - nums[index] in nums[index+1:]:
                comp_index =  index + 1 + nums[index+1:].index(target - nums[index])
                return [index, comp_index]
            
            index += 1
