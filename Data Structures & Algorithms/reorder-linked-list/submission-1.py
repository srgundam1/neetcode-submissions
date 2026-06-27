# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
          # part 1: take 2nd portion of list and reverse it
          # part 2: join the lists

          # find middle of list by using fast and slow pointers
          # when fast reaches the end, slow will be in the middle
          # need 2 temp pointers so we dont break the link

          slow = head
          fast = head.next 
          while fast and fast.next: # while fast is not at end of list
            slow = slow.next
            fast = fast.next.next

          second = slow.next # second half of the list
          prev = slow.next = None

          while second: #reversing second portion of list
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
          first = head
          second = prev
          while second: # because second half is shorter or equal to first
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            # reset pointers
            first = temp1
            second = temp2
        # dont have to return because we changed in-place

        