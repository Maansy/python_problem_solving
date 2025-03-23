#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
# @lc code=end

# Helper functions for testing
def list_to_linked_list(lst): # lst is a list
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head): # head is a ListNode
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Test the solution
s = Solution()
input_list = [1, 1, 2]
head = list_to_linked_list(input_list)
result_head = s.deleteDuplicates(head)
print(linked_list_to_list(result_head))  # Output: [1, 2]
