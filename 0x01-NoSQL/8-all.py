#!/usr/bin/env python3
"""This script list all documents
in a collection of Mongodb usig pymongo
"""

def list_all(mongo_collection):
    """A function that returns all the documents"""
    if mongo_collection.count_documents({}) < 1:
        return []
    return mongo_collection.find()

