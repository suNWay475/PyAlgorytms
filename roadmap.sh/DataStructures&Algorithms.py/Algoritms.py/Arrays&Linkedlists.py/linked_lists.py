# # Linked_lists


# class Car:

#     wheels = 4 

#     def __init__(self , brand , color ):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"name: {self.brand} is driving")

# car1 = Car('Toyota', "red")
# car2 = Car('BMW', "black")

# print(car1.brand)
# print(car2.color)
# car1.drive()

# print(Car.wheels)

# # linked 2
# class Node:
#     def __init__(self, value):
#         self.value = value   
#         self.next = None     


# node1 = Node(10)   # → value=10, next=None
# node2 = Node(20)   # → value=20, next=None

# node1.next = node2 
# # linked 3




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, data):
    # випадок 1 — видаляємо head
        if self.head.data == data:
            self.head = self.head.next

        # випадок 2 — шукаємо елемент
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # пропускаємо елемент
                return
            current = current.next
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' → ')
            current = current.next
        print('None')

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.prepend(0)
ll.delete(1)
ll.print_list()







