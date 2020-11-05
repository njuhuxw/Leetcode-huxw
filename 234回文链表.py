# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(head: ListNode) -> bool:
        temp = []
        x = head
        while x != None:
            temp.append(x.val)
            x = x.next

        return True if temp == temp[::-1] else False
