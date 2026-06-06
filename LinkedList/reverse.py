class Linkedlist:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reversell(head:Linkedlist):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev 
        prev = curr
        curr = next
    return prev