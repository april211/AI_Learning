# 只扫描一次链表，O(1)空间复杂度，返回链表中间的节点

def find_mid(node):
    if not node:
        return None
    if not node.next:
        return node
    fast = slow = node
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

""" 链表有 n 个节点，如果 n 为奇数，那么中间的节点在第 (n + 1) / 2个节点。
如果 n 为偶数，那么中间的节点在第n / 2个节点。
既然如此，如果我们在链表里面有两个指针（引用），其中一个每次移动2个节点，另一个每次移动一个节点。
这样当快的指针移动到了末尾，慢的指针刚刚好指向中间的节点。 """
