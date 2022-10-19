class Node:
    '''
        singlely linked list node
    '''
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

# node_one = Node(1, None)
# # print(node_one)
# # manually inserting nodes
# node_two = Node(2, None)
# node_one.next = node_two
# print(f'first node: {node_one} second node: {node_one.next}')

class LinkedList:
    '''
        singlely linked list manager class
    '''
    def __init__(self):
        # lists start out empty
        self.head = None
        self.tail = None
        # how many nodes exists in the list
        self.size = 0

    def __len__(self):
        # len(list) -> size of the list
        return self.size
    
    def __str__(self):
        # return a meaningful string representaion of our list
        # iterate over the list, concatenante very node's value into a string
        pass

    def insert_front(self, data):
        '''
            create a new node and place it at the front of the list
        '''
        # if this is the first thing in the list
        if len(self) == 0:
            # set the new node to be both the head and the tail of the list
            self.head = Node(data, None)
            self.tail = self.head
        # replace the head with the new node
        else:
            new_node = Node(data, self.head)
            self.head = new_node
        # increment the size of our list
        self.size += 1

    def insert_end(self):
        '''
            create a new node and place it at the end of the list
        '''
        pass

    def insert_after(self):
        '''
            search for a node, and insert a new node after it
        '''
        pass

    

my_list = LinkedList()
print(len(my_list))
my_list.insert_front(5)
my_list.insert_front(4)
my_list.insert_front(3)
print(f'head: {my_list.head}, tail: {my_list.tail}, head.next: {my_list.head.next}')
