# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = cur = lists[0]
        for l in lists[1:]:
            while l:
                if l.val < cur.val:
                    p = cur
                    cur = l
                    l = cur.next


                # t = l
                # count = 0
                # while l.val <= cur.val:
                #     l = l.next
                #     count += 1
                # s = cur
                # cur = t
                # l = s
                # while count:
                #     cur = cur.next
                #     count -= 1

        return  head
