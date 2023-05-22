from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.ans = ListNode()
        ptr = self.ans
        ptr1, ptr2 = l1, l2
        # carry flag
        flag = False
        # start add operation from head to null
        # 从头开始进行加操作
        while ptr1 and ptr2:
            num = ptr1.val + ptr2.val
            if flag:
                num += 1
            if num >= 10:
                flag = True
            else:
                flag = False
            self.temp = ListNode(num % 10)
            ptr.next = self.temp
            ptr = ptr.next
            ptr1, ptr2 = ptr1.next, ptr2.next
        # attach the left nodes to the answer
        # 将剩下的链表添加至末尾
        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        # if the lengths of the two linklists are the same
        # attach 1 to the tail
        # 如果两个链表长度相同 将1添加至末尾
        if not ptr.next and flag:
            ptr.next = ListNode(1)
            return self.ans.next
        ptr = ptr.next
        # judge if the following nodes have carry flags
        # 判断剩余链表项是否需要进位
        while ptr:
            if flag:
                ptr.val += 1
            if ptr.val>= 10:
                flag = True
            else:
                break
            ptr.val = ptr.val % 10
            if not ptr.next and flag:
                ptr.next = ListNode(1)
                break
            ptr = ptr.next
        return self.ans.next
    
def create_linklist(l):
    head = ListNode()
    ptr = head
    for item in l:
        temp = ListNode(item)
        ptr.next = temp
        ptr = ptr.next
    return head.next

if __name__ == '__main__':
    # l1, l2 = [2,4,3], [5,6,4]
    # l1, l2 = [9,9,1],[1]
    l1,l2 = [9,8],[1]
    # l1, l2 = [9,9,9,9,9,9,9],[9,9,9,9]
    linklist1, linklist2 = create_linklist(l1), create_linklist(l2)
    s = Solution()
    ans = s.addTwoNumbers(linklist1, linklist2)
    ptr = ans
    while(ptr):
        print(ptr.val)
        ptr = ptr.next