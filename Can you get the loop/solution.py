"""Solution"""

class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def loop_size(node):
    """
    Finds the size of a loop in a linked list.
    """
    fast = node
    slow = node
    starting_point = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node
            while fast != slow:
                slow = slow.next
                fast = fast.next
            starting_point = slow
            a = 1
            slow = slow.next
            while slow != starting_point:
                slow = slow.next
                a += 1
            return a
    return None
