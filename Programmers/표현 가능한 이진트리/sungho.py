import math
def check_binary_tree(bin_num: str):
    """
    Express the number as a binary tree

    Params
        str bin_num : binary number of number

    Returns
        int : if the number can be expressed as binary tree, return 1.
    """
    depth = math.ceil(math.log2(len(bin_num) + 1))  # depth of complete binary tree

    if len(bin_num) != 2 ** depth - 1:  # setting 2**(depth-1) digit binary
        bin_num = '0' * (2 ** depth - 1 - len(bin_num)) + bin_num

    # check top -> bottom
    parents = [2 ** (depth - 1)]
    while True:
        # check to be able to check next nodes
        if depth == 1:
            break

        # next nodes
        depth -= 1  # top -> bottom
        nodes = []
        # check nodes
        for p in parents:
            if bin_num[p - 1] == '1':  # if parent == '1', it doesn't matter whether there are nodes or not.
                nodes.append(p - 2 ** (depth - 1))
                nodes.append(p + 2 ** (depth - 1))
            else:  # '0'. if parent == '0', all nodes must be dummy nodes(='0')
                if (bin_num[p - 2 ** (depth - 1) - 1] == '1') or (
                        bin_num[p + 2 ** (depth - 1) - 1] == '1'):  # if not dummy node
                    return 0
                else:  # to check next nodes under dummny nodes
                    nodes.append(p - 2 ** (depth - 1))
                    nodes.append(p + 2 ** (depth - 1))

        # next nodes
        parents = nodes

    return 1


def solution(numbers: list) -> list:
    """
    check if the numbers in list can be expressed as a complete binary tree.

    Params
        list numbers : the numbers

    Returns
        list results : all results. if the number can be expressed as binary tree, return 1.
    """
    results = []
    for number in numbers:
        bin_num = bin(number)  # to binary number, 0bXXX
        bin_num = bin_num[2:]  # remove '0b', XXX

        result = check_binary_tree(bin_num)
        results.append(result)

    return results