#!/usr/bin/env python3
from typing import Optional

class Node:
    def __init__(self, name: str, next_node: Optional['Node'] =None):
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
        if not isinstance(value, str):
            raise ValueError('name must be a string')
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
        return f'Node({self.name}, {self.next_node})'

