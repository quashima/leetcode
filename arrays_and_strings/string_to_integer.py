class Solution:
    def myAtoi(self, s: str) -> int:
        # 1
        whitespace_count = 0
        for i1 in list(s):
            if not i1 == " ":
                break
            whitespace_count+=1
        ignore_whitespace = s[whitespace_count:]

        # 2
        signed_str = ''
        integer_str = ignore_whitespace[0:1]
        if integer_str == '+':
            signed_str = '+'

        if integer_str == '-':
            signed_str = '-'
            
        if signed_str:
            ignore_whitespace = ignore_whitespace[1:]

        # 3
        array_str = []
        for i in list(ignore_whitespace):
            if not i.isnumeric():
                break
            array_str.append(i)

        # 4
        if not array_str:
            return 0

        s_integer_str = ''.join(array_str)

        zero_count = 0
        for s in list(s_integer_str):
            if not s == '0':
                break
            zero_count+=1
        ignore_zero_integer_str = s_integer_str[zero_count:]

        # 5
        if not ignore_zero_integer_str:
            return 0
        
        result_integer_str = signed_str + ignore_zero_integer_str

        if int(result_integer_str) < -2147483648:
            return -2147483648

        if int(result_integer_str) > 2147483647:
            return 2147483647
        
        return int(result_integer_str)

solution = Solution()
result = solution.myAtoi('words and 987')
print('Ans: ', result)