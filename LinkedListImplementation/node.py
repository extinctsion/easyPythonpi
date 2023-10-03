class Node:
    """
    Class for creating Nodes of singly linked list
    contains data and next attributes.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None