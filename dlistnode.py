class dlistnode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def reverse(head):
    while head.prev:
        head.prev, head.next = head.next, head.prev
        head = head.prev
    return head


l1 = dlistnode(10)
l2 = dlistnode(20)
l3 = dlistnode(30)
l1.prev = None
l1.next = l2
l2.prev = l1
l2.next = l3
l3.prev = l2
l3.next = None

print(reverse(l1).next.val)
