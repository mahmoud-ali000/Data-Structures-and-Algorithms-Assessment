'''
A balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one

Write down solution in plain eng
1. build a function to check the [height of a node](https://www.programiz.com/dsa/balanced-binary-tree)
2. utilize the funcion in main function
'''

def node_height(node, height=0):
    if not node:
        return height
    height = max(
        node_height(node.left, height+1), node_height(node.right, height+1)
    )
    return height

def check_balanced(node):
    '''O(N logN)'''
    if not node:
        return True
    l = node_height(node.left)
    r = node_height(node.right)
    if abs(l-r) > 1:
        return False
    return check_balanced(node.left) and check_balanced(node.right)

def combined(node, height=0):
    '''O(LogN)'''
    if not node:
        return height, True
    left_h, left_b = combined(node.left, height+1)
    right_h, right_b = combined(node.right, height+1)

    balanced = abs(left_h - right_h) <= 1 and left_b and right_b
    height = max(left_h, right_h)
    return height, balanced


from binary_tree import *

if __name__ == '__main__':
    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, (1,4,7)), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(check_balanced(test_tree))
    print(combined(test_tree)[1])
    
    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(check_balanced(test_tree))
    print(combined(test_tree)[1])

    test_tree = parse_tuple((
        (1, 3, ((0,0,0),0,0)), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(check_balanced(test_tree))
    print(combined(test_tree)[1])

    test_tree = parse_tuple((
        ((1,1,None), 3, ((0,0,0),0,0)), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    display_keys(test_tree)
    print(check_balanced(test_tree))
    print(combined(test_tree)[1])
