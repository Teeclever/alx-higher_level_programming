#!/usr/bin/python3

"""A function that check if an object is an instance or not
"""


def inherits_from(obj, a_class):
    """
      A function that checks if obj is an instance of a subclass of a class
      Args:
      obj: an object
      a_class: any class object

      Returns:
            Ture or false
       """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
