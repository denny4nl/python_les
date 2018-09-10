# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Link:
    def __init__(self):
        self.first = ListNode('head')

    def add(self, value):
        p = self.first
        new_node = ListNode(value)
        while p.next:
            p = p.next
        else:
            p.next = new_node


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = Link()
        result = []
        while True:
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
            if not (l1 or l2):
                break

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            print(num1, num2)
            num = (num1 + num2 + carry) % 10
            carry = int((num1 + num2 + carry) / 10)
            print(num, carry)
            l3.add(num)

        l3 = l3.first.next
        while l3:
            result.append(l3.val)
            l3 = l3.next

        return result


if __name__ == '__main__':
    l1 = Link()
    l1.add(2)
    l1.add(4)
    l1.add(3)
    l1.add(5)
    print(l1)

    l2 = Link()
    l2.add(5)
    l2.add(6)
    l2.add(4)
    print(l2)
    sol = Solution()
    print(sol.addTwoNumbers(l1.first, l2.first))
