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
        # Зберігаємо значення вузла
        self.data = data
        # Вказівник на наступний вузол (за замовчуванням — None)
        self.next = None

class LinkedList:
    def __init__(self):
        # На початку список порожній — head вказує на None
        self.head = None

    def append(self, data):
        """Додає новий вузол у кінець списку."""
        new_node = Node(data)
        # Якщо список порожній — новий вузол стає головою
        if self.head is None:
            self.head = new_node
            return
        # Проходимо до останнього вузла
        current = self.head
        while current.next:
            current = current.next
        # Прикріплюємо новий вузол після останнього
        current.next = new_node

    def prepend(self, data):
        """Додає новий вузол на початок списку."""
        new_node = Node(data)
        # Новий вузол вказує на колишню голову
        new_node.next = self.head
        # Новий вузол стає новою головою
        self.head = new_node

    def delete(self, data):
        """Видаляє перший вузол із заданим значенням."""
        # Випадок 1 — видаляємо head: просто зсуваємо голову на наступний вузол
        if self.head.data == data:
            self.head = self.head.next
            return  # ← виходимо, щоб не продовжувати пошук

        # Випадок 2 — шукаємо елемент у решті списку
        current = self.head
        while current.next:
            if current.next.data == data:
                # Пропускаємо знайдений вузол, з'єднуючи попередній з наступним
                current.next = current.next.next
                return
            current = current.next
        # Якщо елемент не знайдено — нічого не робимо
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:  # заповни
                return True          # заповни
            current = current.next
        return False                  # заповни
    def remove_nth_from_the_end(self, n):

        dummy = Node(0)
        dummy.next = self.head

        fast = dummy
        slow = dummy

        # рухаємо fast на n+1 кроків
        for _ in range(n + 1):
            fast = fast.next

        # рухаємо обидва
        while fast:
            fast = fast.next
            slow = slow.next

        # видаляємо вузол
        slow.next = slow.next.next

        self.head = dummy.next
    def print_list(self):
        """Виводить усі елементи списку у вигляді: 1 → 2 → None."""
        current = self.head
        while current:
            print(current.data, end=' → ')
            current = current.next
        print('None')  # Позначаємо кінець списку


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.remove_nth_from_the_end(2)
ll.print_list()

