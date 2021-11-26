from typing import List

# Time Limit Exceeded
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i1, v1 in enumerate(nums):
#             for i2, v2 in enumerate(nums[1:]):
#                 if target == (v1+v2) and not i1 == (i2+1):
#                     return [i1, (i2+1)]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for _i, _num in enumerate(nums):
            _diff = target - _num
            if _diff in nums and not _i == nums.index(_diff):
                return sorted([_i, nums.index(_diff)])


solution = Solution()
result = solution.twoSum([2,7,11,15], 9)
print('Ans: ', result)