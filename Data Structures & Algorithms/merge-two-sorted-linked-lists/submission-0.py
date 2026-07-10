# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        values = []

        current = list1
        while current:
            values.append(current.val)
            current = current.next

        current = list2
        while current:
            values.append(current.val)
            current = current.next


        values.sort()


        dummy = ListNode(0)
        movingpointer = dummy

        for value in values:
            movingpointer.next = ListNode(value)
            movingpointer = movingpointer.next

        return dummy.next