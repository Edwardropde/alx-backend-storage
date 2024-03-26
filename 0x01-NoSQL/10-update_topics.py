#!/usr/bin/env python3
"""
Task 10 Module
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes topics of collection documents based on the name
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
