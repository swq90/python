# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        l1 = []
        while curA:
            l1.append(curA.val)
            curA = curA.next
        while curB:
            t = curB
            if t:
                l2 = l1[l1.index(t.val):]
            index = 0
            while t and l2:
                if t.val == l2[index]:
                    t = t.next
                    index += 2
                else:
                    l2 = l2[l1.index(curB.val)+1:]
                    break
            if not t and not l2.[index]:return True
            elif t