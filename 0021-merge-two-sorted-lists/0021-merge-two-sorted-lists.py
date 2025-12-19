# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #create new linked list
        
        start = ListNode()
        new_list = start

        while list1 and list2:
            if list1.val<=list2.val:
                new_list.next=list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        if list1:
            new_list.next=list1
        else:
            new_list.next=list2
        return start.next


        #if head(list1) <head(list2):
        #append head(list1) node to head of new linked list, update next node in list1 to be the new head in list1