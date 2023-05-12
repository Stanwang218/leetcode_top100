from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# construct a cycled linklist
def construct_list(l: list, points:list):
    for i, item in enumerate(l):
        if i == 0:
            node = ListNode(item)
            ptr = node
        else:
            temp_node = ListNode(item)
            ptr.next = temp_node
            ptr = ptr.next
    ptr = node
    entry, exit = None, None
    i = 0
    while ptr:
        if i == points[0]:
            entry = ptr
        if i == points[1]:
            exit = ptr
        ptr = ptr.next
        i += 1
    exit.next = entry
    return node

"""
Suppose:
l1 = the length from head to the entry
l2 = the length from entry to the meet point
l3 = the length from meet point to the entry

the distance of the slow pointer = l1 + l2
the distance of the fast pointer = l1 + l2 + l3 + l2
We know the distance of the fast pointer is twice longer than the slow
2(l1 + l2) = l1 + l2 + l3 + l2 =>  l1 = l3

"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while slow and fast and fast.next and slow.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


if __name__ == '__main__':
    s = Solution()
    l = [3,2,0,4]
    # point[0] indicates the entry point
    # point[1] indicates the end point
    point = [1,3]
    linklist = construct_list(l, point)
    ptr = linklist
    print(s.detectCycle(linklist).val)
