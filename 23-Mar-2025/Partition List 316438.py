# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        head1, head2 = left, right

        while head:
            if head.val < x:
                head1.next = head
                head1 = head1.next 
            else:
                head2.next = head
                head2 = head2.next 
            
            head = head.next 
        head1.next = right.next
        head2.next = None
        return left.next

        