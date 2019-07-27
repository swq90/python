# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #         r = ListNode()
        #         a,b = len(l1),len(l2)
        #         n1,n2 = 0,0
        #         if  not a:
        #             return l2
        #         if not b:
        #             return l1
        #         while l1.next:
        #             n1 = n1*10 + l1.val
        #             l1 = l1.next
        #         while l2.next:
        #             n2 = n2*10 +l2.val
        #             l2 = l2.next
        #         n = n1 + n2
        #         while n:
        #             r.val = n

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next