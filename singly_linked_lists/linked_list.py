#!/usr/bin/env python3
"""This module defines the implementation of the LinkedList class."""

from node import Node, NodeNum
from typing import Optional


class LinkedListNum:
    """LinkedList class to manage a singly linked list of Node objects."""
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def print_list(self) -> None:
        """
        Print all elements of the linked list.
        If name is None, print 0.
        """
        current = self.head
        while current:
            print(f'{current.n}')
            current = current.next_node

    def __len__(self) -> int:
        """
        Return the number of elements in the linked list.
        Returns 0 if the list is empty.
        """
        return self.count
        

    def add_node_head(self, n: int) -> NodeNum | None:
        """
        Add a node at the beginning of the linked list.

        Args:
            n (int): The n attribute of the newly created node.

        Returns:
            NodeNum or None: The newly added node, or None if the operation failed.
        """
        try:
            new_node = NodeNum(n)
        except Exception as e:
            return None
        new_node.next_node = self.head
        self.head = new_node
        self.count += 1
        return new_node

    def add_node_end(self, n: int) -> NodeNum | None:
        """
        Add a node at the end of the linked list.

        Args:
            n (int): The n attribute of the newly created node.

        Returns:
            NodeNum or None: The newly added node, or None if the operation failed.
        """
        try:
            new_node = NodeNum(n)
        except Exception as e:
            return None
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.count += 1
        return new_node

    def free_list(self) -> None:
        """
        Free the linked list by removing all references to nodes.
        """
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = None
            current = next_node
        self.head = None
        self.count = 0

    def pop_head_node(self) -> int:
        """
        Delete the head node of a linked list
        Returns:
            n or 0: The head node data, or zero if list is empty
        """
        if self.head:
            tmp = self.head
            self.head = tmp.next_node
            tmp.next_node = None
            self.count -= 1
            return tmp.n
        else:
            return None
    
    def get_node_at_index(self, idx: int) -> Optional['NodeNum']:
        """
        Return node at index idx or None if idx doesn't exist
        """
        if not (idx >= 0 and idx < self.count):
            return None
        current = self.head
        for i in range(idx):
            current = current.next_node
        return current

    def sum_list(self) -> int:
        """Return the sum of all elements in a list or 0 if empty"""
        current = self.head
        total = 0
        while current:
            total += current.n
            current = current.next_node
        return total
    
    def insert_node_at_index(self, idx: int, value: int) -> NodeNum | None:
        """
        Insert node at index idx.
        
        Args:
            idx (int): Position at which to insert (0-based).
            value (int): Value for the new node.

        Returns:
            NodeNum or None: The new node, or None if index is invalid.
        """
        if not (idx >= 0 and idx <= self.count):
            return None
        try:
            if idx == 0:
                return self.add_node_head(value)
            current = self.head
            for i in range(idx - 1):
                current = current.next_node
            new_node = NodeNum(value)
            new_node.next_node = current.next_node
            current.next_node = new_node
            self.count += 1
            return new_node
        except Exception as e:
            return None
    
    def delete_node_at_index(self, idx: int) -> int:
        """
        Delete node at index idx.
        
        Args:
            idx (int): Position at which to delete (0-based).

        Returns:
            1 if it succeeded, -1 if it failed
        """
        if not (idx >= 0 and idx < self.count):
            return -1
        try:
            if idx == 0:
                tmp = self.head
                self.head = tmp.next_node
                self.count -= 1
                return 1
            current = self.head
            for i in range(idx - 1):
                current = current.next_node
            current.next_node = current.next_node.next_node
            self.count -= 1
            return 1
        except Exception as e:
            return -1

class LinkedList:
    """LinkedList class to manage a singly linked list of Node objects."""
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def print_list(self) -> None:
        """
        Print all elements of the linked list.
        If name is None, print 0.
        """
        current = self.head
        while current:
            if current.name:
                print(f'[{current.name_length}] {current.name}')
            else:
                print(f'[0] (nil)')
            current = current.next_node

    def __len__(self) -> int:
        """
        Return the number of elements in the linked list.
        Returns 0 if the list is empty.
        """
        return self.count
        

    def add_node_head(self, name: str) -> Node | None:
        """
        Add a node at the beginning of the linked list.

        Args:
            name (str): The name attribute of the newly created node.

        Returns:
            Node or None: The newly added node, or None if the operation failed.
        """
        try:
            new_node = Node(name)
        except Exception as e:
            return None
        new_node.next_node = self.head
        self.head = new_node
        self.count += 1
        return new_node

    def add_node_end(self, name: str) -> Node | None:
        """
        Add a node at the end of the linked list.

        Args:
            name (str): The name attribute of the newly created node.

        Returns:
            Node or None: The newly added node, or None if the operation failed.
        """
        try:
            new_node = Node(name)
        except Exception as e:
            return None
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.count += 1
        return new_node

    def free_list(self) -> None:
        """
        Free the linked list by removing all references to nodes.
        """
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = None
            current = next_node
        self.head = None
        self.count = 0
