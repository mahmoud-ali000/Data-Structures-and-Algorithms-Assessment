from binary_tree import *

'''
check if a tree-n2 is a subtree of tree-n1:
    create a traversal function to do brute force solution
'''

# not this way, this way wonld not be able to determine whether a part of the list is a tree or what 
def traversal(node):
    '''in-order traversal'''
    if not node:
        return []
    return traversal(node.left) + [node.key] + traversal(node.right)

# try to find a correct way to do it
def check_subtree(n1, n2):
    '''
    ~~brute force in-order traversal the tree n1~~
    use BFS instead
    '''
    # handle wrong input
    if not (type(n1)==type(n2)==Node):
        return False

    queue = [n1]
    while queue:
        current = queue.pop(0)
        if current == n2:
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False
        


if __name__ == '__main__':
    print(f'Node\'s identical through nodes themself {Node(2) == Node(2)}')
    print(f'while link comparison {[1]==[1]}')

    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    n1 = test_tree
    n2 = test_tree.right
    print(check_subtree(n1, n2))
