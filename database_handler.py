# This will handle saving and loading the database information
import csv
import os
from pathlib import Path

# Code duplicate to gui2.py
OUTPUT_PATH = Path(__file__).parent
def get_new_id():
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        last_id = 0
        for row in reader:
            last_id = int(row[0])
        new_id = last_id + 1
    return new_id

def getStatus(id):
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            if int(row[0]) == id:
                return row[5]
    return "none"

def getLatestStatus():
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        last_id = 0
        last_status = ""
        for row in reader:
            last_id = int(row[0])
            last_status = row[5]
        return last_status