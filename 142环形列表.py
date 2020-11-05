# 快慢指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast != None:
        fast = fast.next

        if fast == None:
            break

        fast = fast.next
        slow = slow.next

        if fast == slow:
            break

    # notice
    if fast == None:
        return None

    p1, p2 = slow, head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1
