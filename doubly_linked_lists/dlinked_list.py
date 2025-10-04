#!/usr/bin/env python3

from node import Node

class DoublyLinkedList:
    """
    A doubly linked list implementation.

    This data structure maintains elements in nodes that are linked
    both forward and backward, allowing efficient insertion and deletion
    at both ends, as well as traversal in both directions.

    Attributes:
        __head (Optional[Node]): Reference to the first node in the list.
        __count (int): Number of nodes in the list.

    Methods:
        print_dlist() -> None:
            Print all node values in the list.
        
        __len__() -> int:
            Return the number of nodes in the list.

        add_node_head(n: int) -> Optional[Node]:
            Insert a new node with value `n` at the beginning of the list.

        add_node_end(n: int) -> Optional[Node]:
            Insert a new node with value `n` at the end of the list.

        free_dlist() -> None:
            Clear the entire list, unlinking all nodes.

        get_node_at_index(idx: int) -> Optional[Node]:
            Return the node at position `idx`, or None if out of range.

        sum_dlistint() -> int:
            Return the sum of all integer values in the list.

        insert_node_at_index(idx: int, n: int) -> Optional[Node]:
            Insert a new node with value `n` at position `idx`.
            Returns the new node, or None if index is invalid.

        delete_node_at_index(idx: int) -> int:
            Delete the node at position `idx`.
            Returns 1 if successful, -1 if index is invalid.
    """
    
    def __init__(self) -> None:
        self.__head = None
        self.__count = 0
    
    def print_dlist(self) -> None:
        current = self.__head
        while current:
            print(current.n)
            current = current.next_node
    
    def __len__(self) -> int:
        return self.__count
    
    def add_node_head(self, n: int) -> Node | None:
        try:
            new_node = Node(n)
            if self.__head is None:
                self.__head = new_node
                self.__count += 1
                return new_node
            
            new_node.next_node = self.__head
            self.__head.prev_node = new_node
            self.__head = new_node
            self.__count += 1
            return new_node
        except ValueError:
            return None
    
    def add_node_end(self, n: int) -> Node | None:
        try:
            new_node = Node(n)
            if self.__head is None:
                self.__head = new_node
                self.__count += 1
                return new_node
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
            new_node.prev_node = current
            self.__count += 1
            return new_node
        except ValueError:
            return None
    
    def free_dlist(self) -> None:
        current = self.__head
        while current:
            next_node = current.next_node
            current.prev_node = None
            current.next_node = None
            current = next_node
        self.__head = None
        self.__count = 0
    
    def get_node_at_index(self, idx: int) -> Node | None:
        if not (idx >=0 and idx < self.__count):
            return None
        current = self.__head
        for _ in range(idx):
            current = current.next_node #type: ignore
        return current
    
    def sum_dlistint(self) -> int:
        current = self.__head
        total = 0
        while current:
            total += current.n
            current = current.next_node
        return total
    
    def insert_node_at_index(self, idx: int, n: int) -> Node | None:
        try:
            if not (idx >= 0 and idx <= self.__count):
                return None
            if idx == 0:
                return self.add_node_head(n)
            if idx == self.__count:
                return self.add_node_end(n)
            current = self.get_node_at_index(idx - 1)
            new_node = Node(n)
            new_node.next_node = current.next_node # type: ignore
            current.next_node.prev_node = new_node # type: ignore
            new_node.prev_node = current
            current.next_node = new_node # type: ignore
            self.__count += 1
            return new_node
        except ValueError:
            return None
    
    def delete_node_at_index(self, idx: int) -> int:
        if not (idx >= 0 and idx < self.__count):
            return - 1
        current = self.get_node_at_index(idx)
        if current.prev_node is None: #type: ignore
            self.__head = current.next_node #type: ignore
            if self.__head:
                self.__head.prev_node = None
        elif current.next_node is None: #type: ignore
            current.prev_node.next_node = None #type: ignore
        else:
            current.next_node.prev_node = current.prev_node #type: ignore
            current.prev_node.next_node = current.next_node #type: ignore
        self.__count -= 1
        return 1