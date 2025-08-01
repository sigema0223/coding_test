from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumbers(self, li: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: