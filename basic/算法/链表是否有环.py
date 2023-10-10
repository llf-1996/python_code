"""
判断链表是否有环
"""


class LNode:
    """链表节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.pnext = None


def exitLoop(LList):
    p1 = p2 = LList
    while p2 and p2.pnext:  # 当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        p1 = p1.pnext
        p2 = p2.pnext.pnext
        if p1 == p2:
            return True
    return False


def exist_circle1(head):
    dic = {}
    cursor = head
    count = -1
    while cursor.next:
        if cursor not in dic.values():
            count += 1
            dic[count] = cursor
            cursor = cursor.next
        else:
            return True
    return False


if __name__ == "__main__":
    p0 = LNode(0)
    p1 = LNode(1)
    p2 = LNode(2)
    p3 = LNode(3)
    p4 = LNode(4)
    p5 = LNode(5)
    p0.pnext = p1
    p1.pnext = p2
    p2.pnext = p3
    p3.pnext = p4
    p4.pnext = p5
    p5.pnext = p2
    print(exitLoop(p0))
