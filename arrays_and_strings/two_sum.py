from typing import List
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for _i, _num in enumerate(nums):
            _diff = target - _num
            if _diff in nums and not _i == nums.index(_diff):
                return sorted([_i, nums.index(_diff)])


solution = Solution()
# result = solution.twoSum([2,7,11,15], 9)
result = solution.twoSum([-1,0,1,2,-1,-4], -4)
print('Ans: ', result)