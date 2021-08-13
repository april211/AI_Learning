# 只扫描一次链表，O(1)空间复杂度，返回链表倒数第 k 个节点

def find_reverse_k(node, k):
    if not node or k == 0:
        return None
    front = behind = node
    window = 0
    while front:
        window += 1
        front = front.next
        if window == k:
            break
    else:    # while ... else 语法，如果循环正常结束，就会进入 else
        raise Exception('k 比链表长度还长！')
    while front:
        front = front.next
        behind = behind.next
    return behind

""" 这次两个指针是移动速度是一样的。但是，一种一个指针先移动 k 个节点，然后两个指针再开始同时移动。这样两个指针中间始终会间隔 k 个节点。这样一来，当先走的指针到了None，后走的指针刚刚好走到倒数第 k 个节点。
不过，在解决这道题的时候，需要考虑，k 如果大于链表长度的时候，应该要返回错误信息。 """

""" 他们都是使用了两个指针，通过两个指针之间的节点差来解决问题的。 """
