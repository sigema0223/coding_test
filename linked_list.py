import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length #To check the lenght of list by using len()
    
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length+=1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length+=1

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        res = "Head"
        node = self.head
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res
    
    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False
    
    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        prev = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head: 
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data
    
    def remove(self, target):
        if self.head is None:
            return False
        if self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return True
        
        prev = self.head
        node = self.head.next

        while node is not None:
            if node.data == target:
                prev.next = node.next
                self.length -= 1
                return True
            prev = node
            node = node.next
        return False


if __name__ == "__main__":

    #checking appendleft(self, data) and append(self, data) and print_list(self)
    """
    my_list = LinkedList()
    print(f"Create Linked List and its length is {len(my_list)}")
    print(my_list)
    print()
    for i in range(5):
        my_list.appendleft(i)  
        #my_list.append(i)
        print(f"{i} is added, lenght of list is {len(my_list)}")
        print(my_list)
    my_list.print_list()
    """

    #checking __contanis__(self, target)
    """
    data = list(range(10, 20))
    random.shuffle(data)
    my_list = LinkedList()
    for i in data:
        my_list.append(i)
    my_list.print_list()

    for _ in range(4):
        i = random.randint(5,25)
        if i in my_list:
            print(f"{i} is in the list")
        else:
            print(f"{i} is not in the list")
    """

    #checking popleft(self)
    """
    data = list(range(10, 15))
    random.shuffle(data)
    my_list = LinkedList()
    for i in data:
        my_list.append(i)

    print(f"State of the linked list:\n{my_list}")
    print()

    for _ in range(len(my_list)):
        #print(f"After popping {my_list.popleft()}: length = {len(my_list)}, {my_list}")
        print(f"After popping {my_list.pop()}: length = {len(my_list)}, {my_list}")

    print(f"The value popped when the linked list is empty: {my_list.popleft()}")
    """
    

    #checking remove(self, target)
    lst = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        lst.append(i)

    def display_list():
        print("List now:", lst, end=" ")

    print("Initial list:", lst)
    print("Removing head (10):", lst.remove(10))
    display_list()
    print("Removing middle (30):", lst.remove(30))
    display_list()
    print("Removing tail (50):", lst.remove(50))
    display_list()
    print("Trying to remove value not in list (99):", lst.remove(99))
    display_list()
    lst.remove(20)
    lst.remove(40)
    print("Removed all elements.")
    display_list()
    print("Trying to remove from empty list (10):", lst.remove(10))
    display_list()
    print("=== Test Complete ===")