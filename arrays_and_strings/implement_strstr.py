class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Output Limit Exceeded
        # if needle == '':
        #     return 0

        # _str_str = ''
        # _loop_count = len(haystack) - len(needle) + 1
        # for _i in range(_loop_count):
        #     for _n in range(len(needle)):
        #         _str_str += haystack[_i+_n]
        #     print(_str_str)
        #     if _str_str == needle:
        #         return _i
        #     else:
        #         _str_str = ''
        # return -1

        if needle == '':
            return 0

        _needle_len = len(needle)
        for _i in range(len(haystack) - len(needle) + 1):
            if haystack[_i:_i+_needle_len] == needle:
                return _i
        return -1

solution = Solution()
result = solution.strStr('hello', 'll')
# result = solution.strStr('aaaaa', 'bba')
# result = solution.strStr('', '')
# result = solution.strStr('', 'a')
print('Ans: ', result)