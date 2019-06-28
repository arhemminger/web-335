"""
============================================
; Title:  Updating and Deleting Documents
; Author: Professor Krasso
; Date:  27 June 2019
; Modified by: Andrew Hemminger
; Description: Exercise 9.3 – Updating and Deleting Documents
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

# Update specified document
db.users.update_one(

    {"employee_id":"0011223"},

    {
        "$set":{

            "email":"ahemminger@my365.bellevue.edu"

        }
    }
)

# Output results of updated document
pprint.pprint(db.users.find_one({"employee_id":"0011223"}))