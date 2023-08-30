# https://stackoverflow.com/questions/21211701/given-a-bst-and-its-root-print-all-sequences-of-nodes-which-give-rise-to-the-sa by j.andrew.key

from binary_search_tree import *


def weave_lists(first: list, second: list, results: list, prefix: list) -> None:
    '''
    Recursively Weave the first list into the second list and append it to the results list.
    The prefix list grows by an element with the depth of the call stack.
    Ultimately, either the first or second list will be exhausted and the base case will append a result.
    '''
    # base case
    if not first or not second:
        results.append(prefix + first + second)
        return

    # recursive case
    first_head, first_tail = first[0], first[1:]
    weave_lists(first_tail, second, results, prefix+[first_head])

    second_head, second_tail = second[0], second[1:]
    weave_lists(first, second_tail, results, prefix+[second_head])


def all_sequences(root: Node) -> list:
    '''
    splits the tree into three lists:
        prefix, left and right
    '''
    if root is None:
        return []

    answer = []
    prefix = [root.key]
    left = all_sequences(root.left) or [[]]
    right = all_sequences(root.right) or [[]]

    # At a minimum, left and right must be a list containing an empty list
    # for the following nested loop
    for i in range(len(left)):
        for j in range(len(right)):
            weaved = []
            weave_lists(left[i], right[j], weaved, prefix)
        answer.extend(weaved)

    return answer


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)

    for _list in all_sequences(bst.root):
        print(_list)

    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(1)
    bst.insert(0)
    bst.insert(2)
    bst.insert(5)
    bst.insert(6)

    for _list in all_sequences(bst.root):
        print(_list)
