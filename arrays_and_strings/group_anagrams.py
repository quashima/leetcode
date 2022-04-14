from collections import defaultdict
from curses import keyname
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (<class 'list'>, {}) -> key: value
        ans = defaultdict(list)
        for str in strs:
            # input('eat') -> keyname = ('a','e','t')
            keyname = tuple(sorted(str))
            # keyname（ソートされたstr）と同値であればアナグラムとしてansに格納
            # input('eat') -> ans = {('a','e','t'): ['eat']}
            ans[keyname].append(str)
        return ans.values()

solution = Solution()
result = solution.groupAnagrams(['eat','tea','tan','ate','nat','bat'])
print(result)