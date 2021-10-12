#!/usr/bin/env python3

import json
import csv
from shapely.geometry import Polygon, Point

def add_neighborhood_to_uber_data(uberDataPath, geojsonPath, outputPath):
    # load JSON file containing pickup data
    with open(uberDataPath) as f:
        uber = json.load(f)

    # load GeoJSON file containing sectors
    with open(geojsonPath) as f:
        geojson = json.load(f)

    labelled_pickups = {"pickups": []}

    for pickup in uber['pickups']:
        pt = Point(float(pickup['Lon']), float(pickup['Lat']))
        for feature in geojson['features']:
            polygon = Polygon(feature['geometry']['coordinates'][0])
            if polygon.contains(pt):

                new_pickup = {
                    "date": pickup["Date/Time"],
                    "lat": pickup['Lat'],
                    "lon": pickup['Lon'],
                    "base": pickup['Base'],
                    "neighborhood": feature['properties']['neighborhood']
                }
                labelled_pickups['pickups'].append(new_pickup)
                break

    with open(outputPath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(labelled_pickups, check_circular=False, indent=None))


def add_neighborhood_to_uber_csv_data(uberDataPath, geojsonPath, outputPath):
    # Open a csv reader called DictReader
    with open(uberDataPath, newline='', encoding='utf-8') as in_file:
        uberReader = csv.reader(in_file)

        # "Date/Time","Lat","Lon","Base"

        with open(geojsonPath) as f:
            geojson = json.load(f)
 
        # Open a json writer, and use the json.dumps() function to dump data
        # Open a csv writer called DictWriter
        with open(outputPath, 'w', newline='', encoding='utf-8') as out_file:
            csvWriter = csv.writer(out_file)
            csvWriter.writerow(["u_pickup","u_date","u_lat","u_lon","u_base","u_neighborhood"])
            u_pickup = 0

            for row_data in uberReader:
                if u_pickup == 0:
                    u_pickup = 1
                    continue

                pt = Point(float(row_data[2]), float(row_data[1]))
                for feature in geojson['features']:
                    polygon = Polygon(feature['geometry']['coordinates'][0])
                    if polygon.contains(pt):
                        csvWriter.writerow([u_pickup] + row_data + [feature['properties']['neighborhood']])
                        break
                u_pickup += 1


# Driver Code
 
# Decide the two file paths according to your
# computer system
uberDataPath = r'./uber-tlc-foil-response/uber-trip-data/uber-raw-data-aug14.csv'
geojsonPath = r'./data/nyc-neighbourhoods.geojson'
outputPath = r'./data/uber-raw-data-aug14.csv'
 
# Call the make_json function
# add_neighborhood_to_uber_data(uberDataPath, geojsonPath, outputPath)
add_neighborhood_to_uber_csv_data(uberDataPath, geojsonPath, outputPath)

# min_lon: -74.7733
# max_lon: -72.0666
# min_lat: 40.0729
# max_lat: 42.1166

# "Lat": "40.7594", "Lon": "-73.9722"
# x = 8.7
# y = 11.24
