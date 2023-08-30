from binary_tree import Node

class Node:
    def __init__(self, v):
        '''Singly Linked'''
        self.value = v
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def pop_head(self):
        if self.head is None:
            return False
        theNode = self.head
        self.head = self.head.next
        return theNode
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __str__(self):
        return '-> '.join([str(x.value) for x in self])


def list_of_depths(root:Node) -> list(LinkedList()):
    '''
    BFS
    Assumption: no empty tree

    traverse the level first and store it to list then make it LinkedList
    '''
    level_list = [[root.key]]
    next_queue = []

    while True:
        level_queue = [root.left, root.left]

        level_list.append([])
        for node in level_queue:
            level_list[-1].append(node.key)
        next_queue = []
        
        
# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_04/p03_list_of_depths.py
from collections import deque

class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def create_node_list_by_depth(root):
    '''BFS'''
    levels = {}
    q = deque()
    q.append((root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            # First node in the level
            levels[level] = LinkedList()
        # Nodes already exist
        levels[level].insert(Node(node.name))

        # Push onto queue
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    return levels
    

    

def parse_tuple(data: tuple):
    if isinstance(data, tuple) and len(data) == 3:
        node = BinaryNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = BinaryNode(data)
    return node

def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + '∅')
        return

    if node.left is None and node.right is None:
        print(space*level + str(node.name))
        return
    
    display_keys(node.right, space, level+1)
    print(space*level + str(node.name))
    display_keys(node.left, space, level+1)

if __name__ == '__main__':
    # print(LinkedList().insert(5))
    # create_node_list_by_depth(BinaryNode(5))

    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    for k, v in create_node_list_by_depth(test_tree).items():
        print(f'{k}: {v}')
    
