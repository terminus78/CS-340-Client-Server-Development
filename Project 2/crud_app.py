#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:29:04 2023

@author: shawnway_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username # aacuser
        PASS = password # aacpass
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31468
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create document within database via provided data.
    def create(self, data):
        if data is not None:
            # If the document can't be entered, return False without stopping excecution
            try:
                self.collection.insert_one(data)  # data should be dictionary
            except:
                return False
            return True
        
        # Stop execution if nothing was provided to enter into the database
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read document(s) from database and return as a list.
    def read(self, find_key=None):
        if find_key is not None:
            data = self.collection.find(find_key)
            
            # Return an empty list if not found, otherwise return data
            if data is not None:
                return data
            else:
                return []
        else:
            return self.collection.find()

    # Update document(s) within database
    def update(self, find_key, update_data):
        if find_key is not None and update_data is not None:
            # Update and return mod count. If update fails, return 0
            try:
                update_doc = self.collection.update_many(find_key, update_data)
                return update_doc.modified_count
            except:
                return 0
        
        # Stop execution if nothing was provided to find or to update
        else:
            raise Exception("Nothing to find, because find_key and/or update_data parameter is empty")
        
    # Delete document(s) from database
    def delete(self, find_key):
        if find_key is not None:
            # Delete and return deleted count. If delete fails, return 0
            try:
                delete_doc = self.collection.delete_many(find_key)
                return delete_doc.deleted_count
            except:
                return 0
        
        # Stop execution if nothing was provided to find or to update
        else:
            raise Exception("Nothing to delete, because find_key parameter is empty")

