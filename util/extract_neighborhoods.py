#!/usr/bin/env python3

import json

with open('./js/nyc-neighbourhoods.geo.json') as f:
    geojson = json.load(f)

boroughLookup = {}

for feature in geojson['features']:
    neighborhood = feature['properties']['neighborhood']
    boroughCode = feature['properties']['boroughCode']
    borough = feature['properties']['borough']
    neighborhoodId = feature['properties']["@id"]

    if neighborhood not in boroughLookup:
        boroughLookup[neighborhood] = [borough, boroughCode, neighborhoodId]


with open('./neighborhood-lookup.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(boroughLookup, check_circular=False, indent=None))
