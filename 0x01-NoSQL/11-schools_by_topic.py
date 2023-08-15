#!/usr/bin/env python3
"""A script that defined a func that returns
   List of school having specific topic
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """A func that returns a list of doc with topic """
    return mongo_collection.find({"topic": topic})
