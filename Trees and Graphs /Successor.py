'''
in-order traversal:
left subtree-> current node-> right subtree
'''

from binary_search_tree import *

def successor(node):
    '''
    find the next node (in-order traversal next node) of the given node
    '''
    # check Right
    if node.right != None:
        return node.right
    
    # check what node it is: Left or Right
    if node == node.parent.left:
        return node.parent
    
    # Right
    if node == node.parent.right:
        while node:
            node = node.parent
            if node.parent == None:
                return None

            # check if node is the Left of the parent
            if node == node.parent.left:
                return node.parent


test_cases = [
    (20, 25),
    (9, 12),
    (25, None),
    (5, 9),
    (12, 14), 
    (11, 12),
    (14, 20)
]

if __name__ == '__main__':
    bst = BinarySearchTree()
    for k, _ in test_cases:
        bst.insert(k)

    from binary_tree import display_keys
    display_keys(bst.root)

    for k, next_k in test_cases:
        output = successor(bst.get_node(k))
        if output:
            print( output.key == next_k, f'in:{k} out:{output.key} == {next_k}')
    print('done testing')
