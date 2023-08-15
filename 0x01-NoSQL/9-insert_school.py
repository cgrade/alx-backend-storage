#!/usr/bin/env python3
"""A python function that inserts a new document
   in a collection based on Kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """func that insert document in a MongoDB collection"""
    return mongo_collection.insert(kwargs)
