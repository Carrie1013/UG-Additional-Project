class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class doubleLinked:
    def __init__(self, n):
        self.head = Node(None)
        self.length = 0
        self.size = n

    def is_Empty(self):
        return self.length == 0

    def add(self, value):
        node = Node(value)
        if self.is_Empty():
            node.prev = self.head
            self.head.next = node
            self.length += 1

    def insert_left(self, target_pos, value):
        node = Node(value)
        tmpnode = self.head.next
        while tmpnode.value != target_pos:
            tmpnode = tmpnode.next
        tmpnode.prev.next = node
        node.prev = tmpnode.prev
        node.next = tmpnode
        tmpnode.prev = node
        self.length += 1

    def insert_right(self, target_pos, value):
        node = Node(value)
        tmpnode = self.head.next
        while tmpnode.value != target_pos:
            tmpnode = tmpnode.next
        node.next = tmpnode.next
        node.prev = tmpnode
        if tmpnode.next != None:
            tmpnode.next.prev = node
        tmpnode.next = node
        self.length += 1
        
    def print_list(self, deletion):
        if not self.is_Empty():
            node = self.head.next
            set_a = set(deletion)
            for i in range(self.size):
                if node.value not in set_a:
                    print(node.value, end = ' ')
                node = node.next


def main():
    n = int(input())
    ll = doubleLinked(n)
    ll.add(1)


    for i in range(n-1):
        nums = input().split(' ')
        nums = [int(i) for i in nums]
        if nums[1] == 0:
            ll.insert_left(nums[0], i+2)
        elif nums[1] == 1:
            ll.insert_right(nums[0], i+2)

    m = input()
    deletion = input().split(' ')
    deletion = [int(i) for i in deletion]

    ll.print_list(deletion)

main()