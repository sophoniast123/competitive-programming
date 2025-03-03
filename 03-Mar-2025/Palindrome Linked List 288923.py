# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            if head is None:
                return True
            else:
                slow = head
                fast = head

                while fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next

                prev = None
                curr = slow
                while curr:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node

                first_node = head
                second_node = prev
                while second_node and first_node:
                    if second_node.val != first_node.val:
                        return False
                    first_node = first_node.next
                    second_node = second_node.next
                return True