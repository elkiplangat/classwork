from node import node

'''
BASE CASES:
    end of the node: node.get_next is None
    the node is empty: node.get_data && get_next is None??
    




'''

def to_string(node_chain):
    '''

    :param node_chain:
    :return:
    returns a string that represents the node-chain
    for a completely empty chain, it returns the String EMPTY

    '''
    if not node_chain:
        return "EMPTY"
    elif len(node_chain) == 1:
        return f"{node_chain[0].get_data()}"
    for i in range(len(node_chain)):
        yield node_chain[i].get_data()



    ...

def copy(node_chain):
    '''

    :param node_chain:
    :return:

    creates a new node with the same values in the same order
    This function copies the node chain and return the reference to the first node in the new chain
    '''



    ...
def replace(node_chain, target, replacement):
    '''

    :param node_chain:
    :param target:
    :param replacement:
    :return:

    replaces every occurence of the data target in node_chain with replacement
    '''
    ...
