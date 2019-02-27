def swapPairs1(self, head):
    dummy = p = ListNode(0)
    dummy.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        p.next = tmp
        head = head.next
        p = tmp.next
    return dummy.next
 
# Recursively    
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head
