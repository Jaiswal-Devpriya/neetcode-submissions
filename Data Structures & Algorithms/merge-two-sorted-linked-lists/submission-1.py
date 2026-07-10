# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        movingpointer = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                movingpointer.next = list1
                list1 = list1.next

            else:
                movingpointer.next = list2
                list2 = list2.next

            movingpointer = movingpointer.next

        if list1:
            movingpointer.next = list1

        else:
            movingpointer.next = list2

        return dummy.next