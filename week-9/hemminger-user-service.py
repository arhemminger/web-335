"""
============================================
; Title:  Querying and Creating Documents
; Author: Professor Krasso
; Date:  27 June 2019
; Modified by: Andrew Hemminger
; Description: Exercise 9.2 – Querying and Creating Documents
;===========================================
"""
# import statements
from pymongo import MongoClient
import pprint
import datetime

# Connecting to the local MongoDB instance
client = MongoClient('localhost', 27017)

db = client.web335

# Output client info to terminal
print(client)

# Creating a new user document
user = {

    "first_name": "Marcus",

    "last_name": "Antonius",

    "email": "mantonius@mail.com",

    "employee_id": "0011223",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

# Output user_id to terminal
print(user_id)

# Print specified document
pprint.pprint(db.users.find_one({"employee_id": "0011223"}))
