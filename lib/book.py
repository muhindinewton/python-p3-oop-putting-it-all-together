#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
    @property
    def page_count(self):
        """This is page_count property!"""
        return self._page_count
    
    @page_count.setter
    def page_count (self, page_count):
        """page_count must be an integer"""
        if not  isinstance (page_count, int):
            print("page_count must be an integer")
        
        self._page_count = page_count
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
        pass
    pass
    
        