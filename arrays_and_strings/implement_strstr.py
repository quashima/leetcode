class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
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