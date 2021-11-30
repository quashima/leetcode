from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:

        def toRoman(num_str: int, index: List[int], romans: List[str]) -> str:
            r_dict = dict(zip(index, romans))
            if int(num_str) in r_dict.keys():
                return r_dict[int(num_str)]
            return '' # num_str = 0

        roman_array_r = []
        nums_r = reversed(str(num))
        for i, num in enumerate(nums_r):
            if (i == 0):
                roman_array_r.append(
                    toRoman(
                        num,
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
                    )
                )

            if (i == 1):
                roman_array_r.append(
                    toRoman(
                        num,
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
                    )
                )

            if (i == 2):
                roman_array_r.append(
                    toRoman(
                        num,
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
                    )
                )

            if (i == 3):
                roman_array_r.append(
                    toRoman(
                        num,
                        [1, 2, 3],
                        ['M', 'MM', 'MMM']
                    )
                )

        return ''.join(reversed(roman_array_r))

solution = Solution()
result = solution.intToRoman(1111)
print('Ans: ', result)