# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 05:17:20 2018

@author: sanooj
"""

"""
Python decorators
--  a decorator is just another function 
    which takes a functions and returns one
--  Python allows you to simplify the 
    calling of decorators using the @ symbol
        (this is called “pie” syntax).    
"""
def repeater(old_function):
    
    def new_function(*args, **kwds):
       
        # See learnpython.org/page/Multiple%20Function%20Arguments 
        #for how *args and **kwds works
        
        old_function(*args, **kwds) 
        # we run the old function
        
        old_function(*args, **kwds)
        # we do it twice
    
    return new_function 
# we have to return the new_function,
# or it wouldn't reassign it to the value

######
"""
decorator means

function =  decorator(second_func) 

"""
######




@repeater
def multiply(num1, num2):
     print(num1 * num2)

print("## with decorator")    
multiply(2,3)


def multiply_without_decorator(num1, num2):
     print(num1 * num2)

print("##without decorator")
new_func = repeater(multiply_without_decorator)
print(new_func(2,3))
