from typing import Optional
import ast

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        answer = ListNode()
        current = answer

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = 1 if total > 9 else 0
            current.next = ListNode(total%10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return answer.next
    
def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

if __name__ == "__main__":
    l1_vals = ast.literal_eval(input("Enter first number as a list (e.g. [2,4,3]): "))
    l2_vals = ast.literal_eval(input("Enter second number as a list (e.g. [5,6,4]): "))
    l1 = make_list(l1_vals)
    l2 = make_list(l2_vals)
    result = Solution().addTwoNumbers(l1, l2)

    output = []
    while result:
        output.append(str(result.val))
        result = result.next

    print("Result:", output)