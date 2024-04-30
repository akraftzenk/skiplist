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
        if pointer.next is not None:
            pointer.next.prev = new_node
        pointer.next = new_node

        level = 0
        last_level_node = new_node
        done = False
        while self.__coin_flip() and not done:
            level += 1
            if level > self.height:
                new_level_head = Node(None, None, None, self.levels[self.height], None)
                self.levels.append(new_level_head)
                self.levels[self.height].above = new_level_head
                self.height += 1

                temp = Node(None, new_level_head, element, last_level_node, None)
                last_level_node.above = temp
                new_level_head.next = temp
                done = True
            else:
                while pointer.above is None:
                    pointer = pointer.prev
                pointer = pointer.above

                new_level_node = Node(pointer.next, pointer, element, last_level_node, None)
                if pointer.next is not None:
                    pointer.next.prev = new_level_node
                pointer.next = new_level_node
                last_level_node.above = new_level_node
                last_level_node = new_level_node

    def remove(self, element):
        pointer = self.get(element)
        while pointer is not None:
            if pointer.prev is not None:
                if pointer.next is not None:
                    pointer.next.prev = pointer.prev
                pointer.prev.next = pointer.next

            if pointer.above is not None:
                pointer.above.below = None
                pointer = pointer.above
            else:
                if pointer.next is None:
                    pointer.prev.next = None
                pointer = None
        pointer = self.levels[self.height]
        while pointer.next is None:
            pointer.below.above = None
            self.levels.pop(self.height)
            self.height -= 1
            pointer = self.levels[self.height]

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
        height = self.height
        while height >= 0:
            pointer = self.levels[height].next
            print(" ")
            print("h: " + height.__str__())
            while pointer is not None:
                print(pointer.value, end=" ")
                pointer = pointer.next
            height -= 1


if __name__ == '__main__':
    skipList = SkipList(random.sample(range(1, 101), 100))
    skipList.print()
    print("\n")
    skipList.remove(skipList.levels[skipList.height].next.value)
    skipList.remove(skipList.levels[skipList.height].next.value)
    skipList.print()
