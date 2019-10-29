# remove linkeding list element
# leetcode: https://leetcode.com/problems/remove-linked-list-elements/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
     def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        curr.next = head
        
        pre = curr
        while curr:            
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        
        return dummy.next