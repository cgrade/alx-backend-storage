#!/usr/bin/env python3
"""a script that updates a collecion in mongodb
by changing all the topics of the doc with name

   Takse 3 args:
   Arg1: Mongo_collection
   Arg2: name
   Arg3: topics
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """A func that update a collec in mongodb"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
