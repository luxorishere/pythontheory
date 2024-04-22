class Node:
    def __init__(self, Data = None):
        self.data = Data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, Data):
        new_node = Node(Data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        print("NULL")


#Example to initialize the code
if __name__ == '__main__':
    llist = LinkedList()

    llist.append(1)
    llist.append(2)
    llist.append(3)

    llist.print_list()

            
    