class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        if len(s_list) == 1:
            return 1

        result = 0
        target_length = []
        for n in range(len(s_list)):
            # 重複値がない場合は[target_length]に要素を格納する
            if s_list[n] not in target_length:
                target_length.append(s_list[n])
            # 重複値がある場合は[result]と[target_length]を比較して大きい値を[result]に置き換える
            else:
                if len(target_length) > result:
                    result = len(target_length)
                # 初期化：重複値の次値以降から現ループで処理している値を[target_length]に格納
                # ex. target_length = ['d', 'v'], s_list[n] = 'd'の時、target_lengthには['v', 'd']を格納する
                dupIndex = target_length.index(s_list[n])
                start_length = target_length[dupIndex+1:]
                start_length.append(s_list[n])
                target_length = start_length
            # リストの最終値の場合は[result]と[target_length]を比較し大きい値を[result]に置き換える
            if n == len(s_list)-1:
                if len(target_length) > result:
                    result = len(target_length)
        return result

solution = Solution()
# result = solution.lengthOfLongestSubstring('dvdf')
result = solution.lengthOfLongestSubstring('abcabcbb')
print('Ans: ', result)