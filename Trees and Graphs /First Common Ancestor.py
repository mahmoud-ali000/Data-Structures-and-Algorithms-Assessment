'''
First Common Ancestor 
Q1: First from bottom or from top?
Q2: Parent property in class?
'''

from BinaryTree import *


def length_to_root(node, i=0):
    while node.parent:
        length = length_to_root(node, i+1)
    return length

def first_common_ancestor(n1, n2):
    '''
    Avoid storing additional nodes in a data structure

    Assumption:
        - 2 nodes are given

    Solution:
        1. check length for each node
        (2. ~~iterate through the short compare with the long~~)
        2. double loop through 2 linkedlist
    '''
    current1 = n1
    while current1:
        current2 = n2
        while current2:
            if current1 == current2:
                return current1
            current2 = current2.parent
        current1 = current1.parent
    return False
            


if __name__ == '__main__':
    t = BinaryTree()
    n1 = t.insert(1, None)
    print(n1.key)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    t.insert(7, n3)
    n8 = t.insert(8, n4)
    # 1 -- 3 -- 7
    #    \
    #      2 -- 5
    #         \
    #           4
    #             \
    #               8
    
    print(first_common_ancestor(n5, n8).key == 2)
    print(first_common_ancestor(n5, n3).key == 1)
    print(first_common_ancestor(n8, n4).key == 4)

    n10 = Node(10)
    print(not first_common_ancestor(n8, n10) == 4)

    '''
    time: O(n2)
    space: O(1)
    '''
