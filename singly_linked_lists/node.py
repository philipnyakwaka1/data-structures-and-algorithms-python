#!/usr/bin/env python3
from typing import Optional

class Node:
    def __init__(self, name: Optional[str] = None, next_node: Optional['Node'] = None):
        self.name = name
        self.next_node = next_node
    
    @property
    def name_length(self) -> int:
        """get name length"""
        return len(self.name)
    
    @property
    def name(self) -> str:
        """get string name"""
        return self.__name
    
    @name.setter
    def name(self, value:str):
        """set name"""
        if not isinstance(value, (type(None), str)):
            raise ValueError('name must be a string or None')
        self.__name = value
    
    @property
    def next_node(self) -> Optional['Node']:
        """get next pointer"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value: Optional['Node']):
        """set next"""
        if not isinstance(value, (type(None), Node)):
            raise ValueError('next_node must be an instance of Node or None')
        self.__next_node = value
    
    def __str__(self):
        "print node"
        return f'Node({self.name})'


class NodeNum:
    def __init__(self, n: int, next_node: Optional['NodeNum'] = None):
        self.n = n
        self.next_node = next_node
    
    @property
    def n(self) -> int:
        """get string n"""
        return self.__n
    
    @n.setter
    def n(self, value: int) -> None:
        """set n"""
        if not isinstance(value, int):
            raise ValueError('n must be an integer')
        self.__n = value
    
    @property
    def next_node(self) -> Optional['NodeNum']:
        """get next pointer"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value: Optional['NodeNum']):
        """set next"""
        if not isinstance(value, (type(None), NodeNum)):
            raise ValueError('next_node must be an instance of NodeNum or None')
        self.__next_node = value
    
    def __str__(self):
        "print node"
        return f'Node({self.n})'

