class Node:
    def __init__(self, next, prev, value):
        self.next = next
        self.prev = prev
        self.value = value


class SkipList:

    def __init__(self, list):
        print("turn list into skiplist")

    @classmethod
    def add(self, element):
        print("add")

    @classmethod
    def remove(self, element):
        print("remove")

    @classmethod
    def get(self, element):
        print("got")


if __name__ == '__main__':
    list = []
    node = Node(None, None, 1)
    node2 = Node(None, node, 2)
    node3 = Node(None, node2, 3)
    node.next = node2
    node2.next = node3

    print(node.value)
    print(node.next.value)
    print(node.next.next.value)
    print("\n")

    print(node2.value)
    print(node2.prev.value)
    print(node2.next.value)
    print("\n")

    print(node3.value)
    print(node3.prev.value)
    print(node3.prev.prev.value)

    skipList = SkipList([1,2,3])
    skipList.add(1)
    skipList.get(1)
    skipList.remove(1)