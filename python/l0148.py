"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        def get_len(head):
            n = 0
            while head:
                head = head.next
                n += 1
            return n
        def divide(head):
            n = get_len(head)
            list1 = list2 = head
            for _ in range(n // 2 - 1):
                list2 = list2.next
            tail1 = list2
            list2 = list2.next
            tail1.next = None
            return list1, list2

        def sort_one(head):
            if head is None or head.next is None:
                return head
            # divide
            list1, list2 = divide(head)
            list1 = sort_one(list1)
            list2 = sort_one(list2)
            # merge
            result = current = ListNode(None)
            while list1 or list2:
                if (list1 and list2 and list1.val <= list2.val) or (list1 and not list2):
                    current.next = list1
                    current = current.next
                    list1 = list1.next
                else:
                    current.next = list2
                    current = current.next
                    list2 = list2.next
            current.next = None
            return result.next
        return sort_one(head)

head = current = ListNode(4)
current.next = ListNode(2)
current = current.next
current.next = ListNode(199)
current = current.next
current.next = ListNode(1)
current = current.next
current.next = ListNode(3)

s = Solution()
head = s.sortList(head)
while head:
    print(head.val)
    head = head.next
