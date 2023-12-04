#!/usr/bin/python3

def inherits_from(obj, a_class):
    return any(issubclass(type(obj), cls) for cls in a_class.__mro__)
