# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)

        while head:
            count = 0
            while head.next and head.val == head.next.val:
                head = head.next
                count += 1
            if count:
                head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next
                cur.next = None

        return dummy.next

# 注意line25,line26的顺序