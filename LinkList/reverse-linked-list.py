# Definition for singly-linked list.
#https://leetcode.cn/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre


if __name__ == '__main__':
    s = Solution()
    head = ListNode(val=1)
    two = ListNode(val=2)
    head.next = two
    three = ListNode(val=3)
    two.next = three
    print(s.reverseList(head))