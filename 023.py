#分治法Divide and Conquer，也就是二分法。每次将所有的list两两之间合并，直到所有list合并成一个。
#时间复杂度：2n * k/2 + 4n * k/4 + ... + (2^x)n * k/(2^x) = O(nklogk)，如果用迭代空间复杂
#度为O(1)，用递归则空间复杂度为O(logk)。
class Solution(object):
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
 
        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]
