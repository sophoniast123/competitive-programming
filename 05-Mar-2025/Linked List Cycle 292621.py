# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}

        current = head
        while current:
            if id(current) in hashmap:
                return True 
                break
            hashmap[id(current)] = 1
            current = current.next
        return False