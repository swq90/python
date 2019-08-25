# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2, res = 0, 0, []
        head = cur = ListNode(0)
        while l1:
            s1 = s1*10+l1.val
            l1 = l1.next
        if not s1:
            return l2
        while l2:
            s2 = s2*10+l2.val
            l2 = l2.next
        m = s1+s2

        while m:
            m, b = divmod(m, 10)
            res.append(b)
        while res:
            cur.next = ListNode(res.pop())
            cur = cur.next
        return head.next




    def addTwoNumbers2(self, l1, l2):
        s1, s2, m,head = [],[],0,None

        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next
            if l2:
                s2.append(l2.val)
                l2 = l2.next

        while s1 or s2 or m:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            m, n = divmod(a+b+m, 10)
            node = ListNode(n)
            node.next = head
            head = node
        return head

# 首先想到了第二种方法，但是链表从后往前不熟练，先用了第一种方法
# 又忽略[0][0]返回空
# 先生成listnode   line30
# 后面倒序生成链表，画个图很容易想通