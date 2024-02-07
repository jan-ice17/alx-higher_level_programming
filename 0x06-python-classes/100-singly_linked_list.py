#!/usr/bin/python3
"""
This module contains classes Node and SinglyLinkedList.
"""


class Node:
    """
    This is a class that defines a node of a singly linked list.

    Attributes:
        __data (int): data stored inside the node.
        __next_node (Node): next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        The constructor for the Node class.

        Parameters:
           data (int): The data stored inside the node.
           next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This is a getter for data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This is a setter for data.

        Parameters:
           value (int): The data stored inside the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This is a getter for next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This is a setter for next_node.

        Parameters:
           value (Node): The next node in the linked list.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is a class that defines a singly linked list.

    Attributes:
        __head (Node): head node of the linked list.
    """

    def __init__(self):
        """
        The constructor for the SinglyLinkedList class.
        """
        self.__head = None

    def __str__(self):
        """
        This method returns a string representation of the SinglyLinkedList.
        """
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        A method inserts a new Node into the correct sorted position in the list.

        Parameters:
           value (int): The data of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
