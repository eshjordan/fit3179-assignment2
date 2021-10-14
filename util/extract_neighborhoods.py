#!/usr/bin/env python3

import json
import csv
from shapely.geometry import Polygon, Point

with open('./data/nyc-neighbourhoods.geojson') as f:
    my_geojson = json.load(f)

with open('./data/nta-map.geojson') as f:
    nta_geojson = json.load(f)

# boroughLookup = {}

# for feature in my_geojson['features']:
#     neighborhood = feature['properties']['neighborhood']
#     boroughCode = feature['properties']['boroughCode']
#     borough = feature['properties']['borough']
#     neighborhoodId = feature['properties']["@id"]

#     if neighborhood not in boroughLookup:
#         boroughLookup[neighborhood] = [borough, boroughCode, neighborhoodId]


# with open('./neighborhood-lookup.json', 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(boroughLookup, check_circular=False, indent=None))

neighborhoodLookup = {}

for feature in my_geojson['features']:
    neighborhood = feature['properties']['neighborhood']
    boroughCode = feature['properties']['boroughCode']
    borough = feature['properties']['borough']
    neighborhoodId = feature['properties']["@id"]

    neighborhoodLookup[neighborhood] = []

    for nta in nta_geojson['features']:
        # "ntacode","shape_area","ntaname","shape_leng","boroname","borocode","countyfips"
        ntaName = nta['properties']['ntaname']
        ntaId = nta['properties']['ntacode']
        ntaCountyFips = nta['properties']['countyfips']
        ntaArea = nta['properties']['shape_area']

        neighborhood_centre = Polygon(feature['geometry']['coordinates'][0]).centroid
        for elem in nta['geometry']['coordinates']:
            for poly in elem:
                nta_polygon = Polygon(poly)

                if nta_polygon.contains(neighborhood_centre):
                    if ntaName not in neighborhoodLookup[neighborhood]:
                        neighborhoodLookup[neighborhood].append([ntaName, ntaId, ntaArea, ntaCountyFips])


with open('data/neighborhood-lookup.csv', newline='', encoding='utf-8') as in_file:
    neighborhoodReader = csv.reader(in_file)

    with open('data/neighborhood-lookup-nta.csv', 'w', newline='', encoding='utf-8') as out_file:
        csvWriter = csv.writer(out_file)

        header = True
        for row_data in neighborhoodReader:
            if header:
                csvWriter.writerow(row_data + ["l_nta_name", "l_nta_id", "l_nta_area", "l_nta_county_fips"])
                header = False
                continue
            
            neighborhood = row_data[0]
            if len(neighborhoodLookup[neighborhood]) == 1:
                csvWriter.writerow(row_data + neighborhoodLookup[neighborhood][0])


for key, value in neighborhoodLookup.items():
    if len(value) != 1:
        print(key, value)

# with open('./neighborhood-lookup.json', 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(boroughLookup, check_circular=False, indent=None))
