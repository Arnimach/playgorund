class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create two pointers
        slow = fast = head

        # keep first pointer at
        #  n nodes from the head
        for i in range(n):
            fast = fast.next

        # if n == len(linked list)
        if fast is None:
            return head.next

        # number of nodes right to the fast pointer
        # = (len(list) - n -1)
        # keep moving until end it reached
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow is the node right before nth node from the end
        # update its next pointer
        slow.next = slow.next.next

        return head
