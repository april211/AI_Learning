# 空间复杂度(1)，查询链表是否有环

def find_cycle(node):
    if not node:
        return False

    slow = fast = node
    while fast:
        fast = fast.next
        if not fast:  # 快的指针到了链表末尾，说明没有环
            return False
        if fast is slow:  # 快的指针追上了慢的指针，说明有环
            return True
        fast = fast.next
        if fast is slow:
            return True
        slow = slow.next
    return False

""" 也是一快一慢两个指针，如果链表有环，那么快的指针会绕到慢的指针的后面，然后追上来。
只要看快的指针是否跟慢的指针重合，就知道是否有环了 """
