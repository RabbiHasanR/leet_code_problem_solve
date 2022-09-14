from platform import node


class Node: 
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = Node()
    
    def prepend(self, data):
        current_node = self.head.next
        new_node = Node(data,current_node)
        self.head.next = new_node
    
    def append(self,data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
            
        current_node.next = node

    def search(self,data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def insert(self,data, new_node):
        if self.head.next is None:
            self.head.next = Node(new_node)
            return
        previous_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                previous_node = current_node
                current_node = current_node.next
                break
            current_node = current_node.next
        previous_node.next =Node(new_node, current_node)
    
    def __repr__(self) -> str:
        nodes = []

        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)

    def remove(self,item):
        previous_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return None
        
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next


L = [5,6,8,2,3,8,9]

singleLinkedList = SingleLinkedList()
for l in L:
    singleLinkedList.append(l)

print(singleLinkedList)

print('search:', singleLinkedList.search(10))
print('insert:', singleLinkedList.insert(2,10))
print('After Insert:',singleLinkedList)
print('remove:',singleLinkedList.remove(8))
print('After Remove:',singleLinkedList)
        
