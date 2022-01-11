from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = ''
        sum2 = ''

        for s1 in reversed(l1):
            sum1 += str(s1)

        return sum1

solution = Solution()
# result = solution.twoSum([2,7,11,15], 9)
result = solution.addTwoNumbers([2,4,3], [5,6,4])
print('Ans: ', result)