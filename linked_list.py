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



if __name__ == "__main__":
    my_list = LinkedList()
    print(f"Create Linked List and its length is {len(my_list)}")
    print()
    for i in range(5):
        my_list.appendleft(i)  
        #my_list.append(i)
        print(f"{i} is added, lenght of list is {len(my_list)}")

    my_list.print_list()