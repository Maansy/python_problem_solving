#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import list, Optional

# class Solution:
#     def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
#         l1 = reversed(l1)
#         l2 = reversed(l2)
#         l1_num = ""
#         l2_num = ""
#         for i in l1:
#             l1_num += str(i)
#         for i in l2:
#             l2_num += str(i)
#         sum = int(l1_num) + int(l2_num)
#         sum = str(sum)[::-1]
#         lst = [int(d) for d in sum]
#         return lst
        
            
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                print(l1.val)
                carry += l1.val
                l1 = l1.next
            if l2:
                print(l2.val)
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10
        return dummy.next

s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(s.addTwoNumbers(l1, l2))
        
# @lc code=end

