# Problem 20: Linked List Reversal (with recursion!)


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# Linked List Stack (last in last out)
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print(self):
        cursor = self.head
        while cursor:
            print(cursor.data)
            cursor = cursor.next

    def reverse(self, cursor=None):
        if cursor:
            if cursor.next:
                self.reverse(cursor.next)
            print(cursor.data)
        else:
            self.reverse(self.head)


# Populates the linked list stack with a basic python list
L = LinkedList()
for node_data in [1, 2, 3, 4]:
    L.insert(node_data)

print('List:')
L.print()
print()

print('Reversed List:')
L.reverse()
print()
