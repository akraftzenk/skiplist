import random


class Node:
    def __init__(self, next, prev, value, below, above):
        self.next = next
        self.prev = prev
        self.value = value
        self.below = below
        self.above = above


class SkipList:
    def __init__(self, list_to_convert):
        self.height = 0
        self.level_zero_head = Node(None, None, None, None, None)
        self.levels = [self.level_zero_head]
        for item in list_to_convert:
            self.add(item)

    def add(self, element):
        pointer = self.levels[self.height]
        level = self.height
        while level > 0:
            while pointer.next is not None and pointer.next.value < element:
                pointer = pointer.next
            level -= 1
            pointer = pointer.below

        while pointer.next is not None and pointer.next.value < element:
            pointer = pointer.next
        new_node = Node(pointer.next, pointer, element, None, None)
        pointer.next = new_node

        level = 0
        last_level_node = new_node
        while self.__coin_flip():
            level += 1
            if level > self.height:
                new_level_head = Node(None, None, None, self.levels[self.height], None)
                self.levels.append(new_level_head)
                self.levels[self.height].above = new_level_head
                self.height += 1

                temp = Node(None, new_level_head, element, last_level_node, None)
                last_level_node.above = temp
                last_level_node = temp
                new_level_head.next = last_level_node
            else:
                while pointer.above is None:
                    pointer = pointer.prev
                pointer = pointer.above
                new_level_node = Node(pointer.next, pointer, element, last_level_node, None)
                pointer.next = new_level_node
                last_level_node.above = new_level_node
                last_level_node = new_level_node

    def remove(self, element):
        print("remove")

    def get(self, element):
        pointer = self.levels[self.height]
        level = self.height
        while level > 0:
            while pointer.next is not None and pointer.next.value < element:
                pointer = pointer.next
            level -= 1
            pointer = pointer.below
        while pointer.next is not None and pointer.next.value < element:
            pointer = pointer.next
        if pointer.next is None or pointer.next.value is not element:
            return None
        if pointer.next.value is element:
            return pointer.next

    def __coin_flip(self):
        return random.choice([0, 1]) == 0

    def print(self):
        print("Total height: " + self.height.__str__())
        for i in range(self.height + 1):
            pointer = self.levels[i].next
            print("h: " + i.__str__())
            while pointer is not None:
                print(pointer.value)
                if i > 0:
                    print("below : " + pointer.below.value.__str__())

                if pointer.above is not None:
                    print("above : " + pointer.above.value.__str__())
                pointer = pointer.next


if __name__ == '__main__':
    skipList = SkipList([1, 2, 3, 4, 5, 6, 7, 8, 10, 15])

    # print(skipList.print())
    # skipList.add(1)
    # result = skipList.get(9)
    # if result is None:
    #     print(result)
    # else:
    #     print(result.value)
    #     print(result.prev.value)
    #     print(result.next.value)
    # skipList.remove(1)
    # skipList.add(9)
    # result = skipList.get(9)
    # if result is None:
    #     print(result)
    # else:
    #     print(result.value)
    #     print(result.prev.value)
    #     print(result.next.value)
    #
    skipList.print()
    print("\n")
    skipList2 = SkipList([])
    skipList2.add(10)
    skipList2.add(0)
    skipList2.print()
