class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        
        for i in range(n):
            complement = target - nums[i]
            if complement in dict1:
                return [dict1[complement] + 1, i + 1]
            dict1[nums[i]] = i