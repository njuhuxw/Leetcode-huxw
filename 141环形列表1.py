# 快慢指针，跟142同

# class ListNode:
def __init__(self, x):
    self.val = x
    self.next = None


def hasCycle(head) -> bool:
    fast, slow = head, head

    while fast != None:
        fast = fast.next
        if fast == None:
            break

        fast = fast.next
        slow = slow.next

        if fast == slow:
            break
    if fast == None:
        return None

    p1, p2 = slow, head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1
