class Resource:

    def __init__(self, name: str, resource_type:str):
        self.name = name
        self.resource_type = resource_type

    def __del__(self):
        print(f"Ресурс {self.name} типа {self.resource_type} удален.")

r1 = Resource("Соединение1", "подключение к базе данных")
r2 = Resource("Соединение2", "подключение к базе данных")

for _ in range(1,11):
    print(_)
    if _ == 5:
        del r2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def len(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    def append(self, obj):
        new_node = Node(obj)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
        end = new_node

    def remove(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        
        if index == 0:
            self.remove_first_node()
        else:
            while current_node is not None and position < index - 1:
                position += 1
                current_node = current_node.next
            
            if current_node is None or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next