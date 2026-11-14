
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Recursively add all numbers
    def recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self.recursive_sum(node.next)

    # Reverse the list recursively
    def recursive_reverse(self, node):
        if node is None or node.next is None:
            return node

        new_head = self.recursive_reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head

    # Recursively search for a number
    def recursive_search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self.recursive_search(node.next, target)

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values))


# MAIN PROGRAM
my_list = LinkedList()

for number in [10, 20, 30, 40, 50]:
    my_list.insert(number)

print("Original list:")
my_list.display()

print("Sum:", my_list.recursive_sum(my_list.head))

print("Searching for 30:")
print(my_list.recursive_search(my_list.head, 30))

my_list.head = my_list.recursive_reverse(my_list.head)

print("Reversed list:")
my_list.display()
