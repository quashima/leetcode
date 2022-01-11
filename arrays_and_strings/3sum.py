from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result_2darray = []
        results = []
        duplicat_v = []

        #  Time Limit Exceeded
        # for _i1, _num1 in enumerate(nums):
        #     for _i2, _num2 in enumerate(nums[1:]):
        #         _i2t = _i2 + 1
        #         for _i3, _num3 in enumerate(nums[2:]):
        #             _i3t = _i3 + 2
        #             if _num1 + _num2 + _num3 == 0:
        #                 if not _i1 == _i2t and not _i1 == _i3t and not _i2t == _i3t:
        #                     print(_i1, _i2t, _i3t)
        #                     _three_sum = sorted([_num1, _num2, _num3])
        #                     if _three_sum not in result_2darray:
        #                         result_2darray.append(_three_sum)
        # return result_2darray

        # Time Limit Exceeded 
        # if 2 >= len(nums):
        #     return []

        # _nums_s = sorted(nums)
        # for _i1, _num1 in enumerate(_nums_s):
        #     if _num1 in duplicat_v:
        #         duplicat_v.append(_num1)
        #     for _i2, _num2 in enumerate(_nums_s[1:]):
        #         _i2t = _i2 + 1
        #         if _i1 == _i2t:
        #             continue

        #         _num3 = -(_num1+_num2)
        #         if _num3 in _nums_s and _i1 != _i2t:
        #             _i3s = [_i for _i, _n in enumerate(_nums_s) if _n == _num3]
        #             if _i1 not in _i3s and _i2t not in _i3s:
        #                 _three_sum = sorted([_num1, _num2, _num3])
        #                 if _three_sum not in result_2darray:
        #                     result_2darray.append(_three_sum)
        #             elif len(_i3s) >= 3 and _num1 == 0 and _num2 == 0 and _num3 == 0:
        #                 if [0,0,0] not in result_2darray:
        #                     result_2darray.append([0,0,0])    
        # return result_2darray

        # if 2 >= len(nums):
        #     return []

        # # _nums_s = sorted(nums)
        # for _i1, _num1 in enumerate(nums):
        #     # if _num1 in duplicat_v:
        #     #     duplicat_v.append(_num1)
        #     for _i2, _num2 in enumerate(nums[1:]):
        #         _i2 += 1
        #         _num3 = -_num1 + -_num2
        #         if _num3 in nums:
        #             _three_sum = sorted([_num1, _num2, _num3])
        #             if _three_sum not in result_2darray and _i1 != _i2:
        #                 _i3s = [_i for _i, _n in enumerate(nums) if _n == _num3]
        #                 if _i1 not in _i3s and _i2 not in _i3s:
        #                     result_2darray.append(_three_sum) 
        #                 elif len(_i3s) >= 3 and _num1 == 0 and _num2 == 0 and _num3 == 0:
        #                     result_2darray.append([0,0,0])
        # return result_2darray

        for _i, _n in enumerate(nums):
            # if _n not in duplicat_v:
            #     duplicat_v.append(_n)
                _dict = self.twoSum(nums, -_n)
                print(_dict)

                if _dict is None:
                    continue

                _indexs = list(_dict.keys())
                print('_indexs', _indexs)
                print('_i', _i)
                if _i not in _indexs:
                    _3sum = list(_dict.values())
                    _3sum.append(_n)
                    _3sum.sort()
                    if _3sum not in results:
                        results.append(_3sum)
        return results

    def twoSum(self, nums: List[int], target: int):
        for _i, _num in enumerate(nums):
            _diff = target - _num
            if _diff in nums and not _i == nums.index(_diff):
                return dict(sorted({ _i: _num, nums.index(_diff): _diff }.items(), key=lambda i: i[0])) # key sort

solution = Solution()
result = solution.threeSum([-1,0,1,2,-1,-4])
# result = solution.threeSum([0,0,0]) # 237
# max = 
# result = solution.threeSum([-1,0,1,0])
# result = solution.threeSum([-2,0,1,1,2])
print('Ans: ', result)