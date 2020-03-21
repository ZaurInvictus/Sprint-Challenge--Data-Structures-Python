from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        print("2", self.current, self.storage.tail)
        if len(self.storage) >= self.capacity:
            print(self.current, self.storage.tail)
            if self.current is self.storage.tail:
                self.current = self.storage.head
                self.storage.head.value = item
            else:
                self.current.next.value = item
                self.current = self.current.next

        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        for i in range(0, self.storage.length):
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
