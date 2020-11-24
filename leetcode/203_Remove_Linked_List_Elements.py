class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(self, head: ListNode, val: int) -> ListNode:
    if not head: return head
    if head.val == val:
        head = self.removeElements(head.next, val)
    else:
        head.next = self.removeElements(head.next, val)
    return head