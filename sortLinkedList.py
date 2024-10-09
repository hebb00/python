# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        myList = ListNode()
        a = list1
        b = list2
        if a == None and b == None:
            return None
        if a == None:
            return b
        if b == None:
            return a
        while a and b:
            if a.val < b.val:
                myList = a
                a = a.next
                print('here a',myList.val)
            else:
                myList=b
                b= b.next
                print('here b',myList.val)
            myList = myList.next
        print(myList)
 
        return myList
    
if __name__ == "__main__":
    l = ListNode()
    ll=ListNode()
    l.val=8
    ll.val=9
    mergeTwoLists(l,ll)
