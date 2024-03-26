#!/usr/bin/env python3
"""
Task 9 Module
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document in collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
