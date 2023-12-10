class Node:
    def __init__(self,val):
        self.val = val
        self.next = 0

    @staticmethod
    def get_sum(head):
        ans = 0
        while head:
            ans += head.val
            head = head.next

        return ans

    def get_sum1(self,head):
        if not head:
            return 0

        return head.val + self.get_sum1(head.next)


one = Node(1)
two = Node(2)
three = Node(3)

one.next = two
two.next = three

head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)


print(head.get_sum(head))
print(head.get_sum1(head))

    