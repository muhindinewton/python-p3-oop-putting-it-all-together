#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
        
    @property
    def size(self):
        """This is size property!"""
        return self._size
    
    @size.setter
    def size (self, size):
        """size must be an integer"""
        if not  isinstance (size, int):
            print("size must be an integer")
        self._size = size
        
    def cobble(self, condition = "used"):
        self.condition = condition
        print("Your shoe is as good as new!")
        self.condition = "New"
        pass
    
