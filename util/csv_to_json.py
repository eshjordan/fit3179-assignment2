#!/usr/bin/env python3

import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {"pickups": []}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for row_data in csvReader:
             
            data["pickups"].append(row_data)
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, check_circular=False, indent=None))

# def make_csv(csvFilePath, jsonFilePath):
    
#     with open(jsonFilePath, encoding='utf-8') as jsonf:
#         data = json.load(jsonf)
    
#     # Open a csv writer called DictWriter
#     with open(csvFilePath, 'w', newline='', encoding='utf-8') as csvf:
#         fieldnames = data["pickups"][0].keys()
#         csvWriter = csv.DictWriter(csvf, fieldnames=fieldnames)
#         csvWriter.writeheader()
         
#         # Convert each row into a dictionary
#         # and add it to data
#         for row_data in data["pickups"]:
#             csvWriter.writerow(row_data)

def make_csv(csvFilePath, pickupFile, jsonFilePath):
    
    with open(jsonFilePath, encoding='utf-8') as jsonf:
        data = json.load(jsonf)

    neighborhood_pickups = {}

    with open(pickupFile, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row_data in csvReader:
            neighborhood = row_data['u_neighborhood']
            if neighborhood in neighborhood_pickups:
                neighborhood_pickups[neighborhood] += 1
            else:
                neighborhood_pickups[neighborhood] = 1
    
    # Open a csv writer called DictWriter
    with open(csvFilePath, 'w', newline='', encoding='utf-8') as csvf:
        csvWriter = csv.DictWriter(csvf, fieldnames=['neighborhood', 'borough', 'boroughId', 'neighborhoodId', 'pickups'])
        csvWriter.writeheader()
        
        # Convert each row into a dictionary
        # and add it to data
        for neighborhood, value in data.items():
            pickups = neighborhood_pickups[neighborhood] if neighborhood in neighborhood_pickups else 0
            row = {'neighborhood': neighborhood, 'borough': value[0], 'boroughId': value[1], 'neighborhoodId': value[2], 'pickups': pickups}
            csvWriter.writerow(row)

         
# Driver Code
 
# Decide the two file paths according to your
# computer system
# csvFilePath = r'data/new-modified-uber-raw-data-apr14.csv'
# jsonFilePath = r'data/BACKUP_uber-data-with-neighborhoods.json'

csvFilePath = r'nyc-wrangling/neighborhood-lookup.csv'
pickupFile = r'data/new-modified-uber-raw-data-apr14.csv'
jsonFilePath = r'nyc-wrangling/neighborhood-lookup.json'
 
# Call the make_json function
# make_json(csvFilePath, jsonFilePath)
make_csv(csvFilePath, pickupFile, jsonFilePath)
