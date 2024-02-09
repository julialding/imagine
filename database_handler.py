# This will handle saving and loading the database information
import csv
import os
from pathlib import Path

# Code duplicate to gui2.py
OUTPUT_PATH = Path(__file__)

def saveIdsToCSV(ids):
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        rows = [row for row in reader if int(row[0]) in ids]

    with open(os.path.join(OUTPUT_PATH.parent, "output.csv"), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def getTopRow():
    with open(os.path.join(OUTPUT_PATH.parent, "output.csv"), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            return row

def runRAG(text):
    # run RAG code here with AI

    #get list of ids
    # saveIdsToCSV()
    return True # when complete

def get_new_id():
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        last_id = 0
        for row in reader:
            last_id = int(row[0])
        new_id = last_id + 1
    return new_id

def getLatestId():
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        last_id = 0
        for row in reader:
            last_id = int(row[0])
        return last_id

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

import os

def updateLatestData(text, significance):
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        data = file.readlines()
    
    if data:
        last_line_columns = data[-1].strip().split(',')
        last_line_columns[5] = text  # 'significance' column
        last_line_columns[6] = significance
        data[-1] = ','.join(last_line_columns) + '\n'
    else:
        print("The file is empty or an error occurred reading the data.")
    
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'w') as file:
        file.writelines(data)
