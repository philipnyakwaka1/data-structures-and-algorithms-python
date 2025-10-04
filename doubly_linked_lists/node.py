#!/usr/bin/env python3

from typing import Optional
class Node:
    """
    A Node in a doubly linked list.

    Attributes:
        n (int): The value stored in the node.
        prev_node (Optional[Node]): Reference to the previous node in the list.
        next_node (Optional[Node]): Reference to the next node in the list.
    """

    __slots__ = ('__n', '__prev_node', '__next_node')

    def __init__(self, n: int, prev: Optional['Node']=None, next: Optional['Node']=None):
        """
        Initialize a Node with a value and optional previous and next references.

        Args:
            n (int): The value of the node.
            prev (Optional[Node]): The previous node. Defaults to None.
            next (Optional[Node]): The next node. Defaults to None.
        """

        self.n = n
        self.prev_node = prev
        self.next_node = next
    
    @property
    def n(self) -> int:
        """Get the integer value of the node."""
        return self.__n

    @n.setter
    def n(self, val: int) -> None:
        """Set the integer value of the node."""
        if not isinstance(val, int): # type: ignore
            raise ValueError('n must be an integer')
        self.__n = val

    @property
    def prev_node(self) -> Optional['Node']:
        """Get the previous node reference."""
        return self.__prev_node

    @prev_node.setter
    def prev_node(self, val: Optional['Node']) -> None:
        """Set the previous node reference."""
        if not isinstance(val, (type(None), Node)): #type: ignore
            raise ValueError('prev_node must be an instance of Node or None')
        self.__prev_node = val

    @property
    def next_node(self) -> Optional['Node']:
        """Get the next node reference."""
        return self.__next_node

    @next_node.setter
    def next_node(self, val: Optional['Node']) -> None:
        """Set the next node reference."""
        if not isinstance(val, (type(None), Node)): #type: ignore
            raise ValueError('next_node must be an instance of Node or None')
        self.__next_node = val
    
    def __repr__(self) -> str:
        """Return a string representation of the node for debugging."""
        prev_id = id(self.prev_node) if self.prev_node else None
        next_id = id(self.next_node) if self.next_node else None
        return f"Node(n={self.n}, prev={prev_id}, next={next_id})"