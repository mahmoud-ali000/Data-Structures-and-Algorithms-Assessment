'''
https://www.geeksforgeeks.org/binary-search-tree-data-structure/

- The left subtree of a node contains only nodes with keys lesser than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- the left and right subtree each must also be a BST
'''

def validate_bst(node):
    '''
    DFS:
        check BST from the bottom of the tree
    
    Assumption: let's ignore the None node for now
    '''

    if not node:
        return True

    if node.left and node.right:
        if node.left.key <= node.key <= node.right.key:
            return validate_bst(node.left) and validate_bst(node.right)
    elif node.left:
        if node.left.key <= node.key:
            return validate_bst(node.left)
    elif node.right:
        if node.key <= node.right.key:
            return validate_bst(node.right)
    elif not node.left and not node.right:
        return True

    return False

def validate_BST_strict(node, min_val=None, max_val=None):
    '''
    ALL left nodes must be less than or equal to the current node
    ALL right nodes must be greater than the current node
    '''
    if not node:
        return True
    if (min_val and node.key < min_val) or (max_val and node.key >= max_val):
        return False
    
    return validate_BST_strict(node.left, min_val, node.key) and validate_BST_strict(node.right, node.key, max_val)


from binary_tree import *

if __name__ == '__main__':
    test_tree = parse_tuple((
        (9, 10, 25), 20, 30
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))

    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, (1,4,7)), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))

    test_tree = parse_tuple((
        (1, 3, 4), 8, (9, 10, (11, 13, 14))
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))

    test_tree = parse_tuple((
        (1, 3, 4), 8, ( (7, 8, 9), 10, (11, 13, 14) )
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))

    test_tree = parse_tuple((
        (1, 3, None), 8, ( (7, 8, 9), 10, (11, 13, 14) )
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))
    
    test_tree = parse_tuple((
        (1, 3, ((0,0,0),0,0)), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))
    
    test_tree = parse_tuple((
        ((1,1,None), 3, ((0,0,0),0,0)), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(validate_bst(test_tree))
    print(validate_BST_strict(test_tree))
    
