
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        
        return ','.join(nodes)

    def prepend(self,data):
        node = Node(data, self.head.next)
        self.head.next = node

    def append(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def search(self, data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def remove(self,data):
        previous_node = self.head
        current_node = previous_node.next
        while current_node:
            if current_node.data == data:
                break
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return None
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next

    def insert(self,data,new_data):
        new_node = Node(new_data)
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def size(self):
        count = 0
        current_node = self.head.next
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def reverse(self):
        prev, curr = None, self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


        



li = LinkedList()
li.prepend(1)
li.prepend(2)
li.prepend(3)
li.append(4)
li.append(5)
print(li)
print(li.search(7))
li.remove(3)
print(li)
li.insert(1,6)
print(li)
print(li.size())
li.reverse()
print(li)