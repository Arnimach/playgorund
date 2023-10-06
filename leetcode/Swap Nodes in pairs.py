# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):

        # if no node in the list
        # return head
        if not head:
            return head

        # return head, if len == 1
        if head.next is None:
            return head

        # create four pointers
        cur = head  # first
        next_ = cur.next   # second
        head = next_   # and change the head pointer after first swap
        last = next_.next  # third

        # swap by changing next pointers
        cur.next = last
        next_.next = cur
        # link to the previous part after swap occurs
        prev = cur
        # change current
        cur = last

        # repeat this until pairs exist
        while cur and cur.next:
            next_ = cur.next
            last = next_.next
            cur.next = last
            next_.next = cur
            prev.next = next_
            prev = cur
            cur = last

        return head
