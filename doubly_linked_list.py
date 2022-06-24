from tkinter.messagebox import NO


class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        
        return ','.join(nodes)
    
    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node
        if first_node:
            first_node.prev = new_node

    def append(self,data):
        new_node = Node(data)
        current_node = self.head.next
        if current_node is None:
            new_node.prev = current_node
            self.head.next = new_node
            return
            
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def search(self, data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        
        if node.next:
            node.next.prev = node.prev

    def remove(self, data):
        node = self.search(data)
        print('search:', node)
        if node is None:
            return None
        self.remove_node(node)

dl = DoublyLinkedList()
dl.prepend(1)
dl.prepend(2)
dl.append(3)
dl.append(4)
dl.prepend(5)
print(dl)
print(dl.search(3))
dl.remove(4)
print(dl)
