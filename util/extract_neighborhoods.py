#!/usr/bin/env python3

import json
import csv
from shapely.geometry import Polygon, Point

# with open('./data/nyc-neighbourhoods.geojson') as f:
#     my_geojson = json.load(f)

# with open('./data/nta-map.geojson') as f:
#     nta_geojson = json.load(f)

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

# neighborhoodLookup = {}

# for feature in my_geojson['features']:
#     neighborhood = feature['properties']['neighborhood']
#     boroughCode = feature['properties']['boroughCode']
#     borough = feature['properties']['borough']
#     neighborhoodId = feature['properties']["@id"]

#     neighborhoodLookup[neighborhood] = []

#     for nta in nta_geojson['features']:
#         # "ntacode","shape_area","ntaname","shape_leng","boroname","borocode","countyfips"
#         ntaName = nta['properties']['ntaname']
#         ntaId = nta['properties']['ntacode']
#         ntaCountyFips = nta['properties']['countyfips']
#         ntaArea = nta['properties']['shape_area']

#         neighborhood_centre = Polygon(feature['geometry']['coordinates'][0]).centroid
#         for elem in nta['geometry']['coordinates']:
#             for poly in elem:
#                 nta_polygon = Polygon(poly)

#                 if nta_polygon.contains(neighborhood_centre):
#                     if ntaName not in neighborhoodLookup[neighborhood]:
#                         neighborhoodLookup[neighborhood].append([ntaName, ntaId, ntaArea, ntaCountyFips])


# with open('data/neighborhood-lookup.csv', newline='', encoding='utf-8') as in_file:
#     neighborhoodReader = csv.reader(in_file)

#     with open('data/neighborhood-lookup-nta.csv', 'w', newline='', encoding='utf-8') as out_file:
#         csvWriter = csv.writer(out_file)

#         header = True
#         for row_data in neighborhoodReader:
#             if header:
#                 csvWriter.writerow(row_data + ["l_nta_name", "l_nta_id", "l_nta_area", "l_nta_county_fips"])
#                 header = False
#                 continue
            
#             neighborhood = row_data[0]
#             if len(neighborhoodLookup[neighborhood]) == 1:
#                 csvWriter.writerow(row_data + neighborhoodLookup[neighborhood][0])


# for key, value in neighborhoodLookup.items():
#     if len(value) != 1:
#         print(key, value)

# with open('./neighborhood-lookup.json', 'w', encoding='utf-8') as jsonf:
#     jsonf.write(json.dumps(boroughLookup, check_circular=False, indent=None))

populationLookup = {}

# p_borough,p_year,p_fips_county_code,p_nta code,p_nta_name,p_population

with open('data/population-by-nta.csv', newline='', encoding='utf-8') as pop_file:
    populationReader = csv.reader(pop_file)
    for row_data in populationReader:
        p_borough = row_data[0]
        p_year = row_data[1]
        p_fips_county_code = row_data[2]
        p_nta_code = row_data[3]
        p_nta_name = row_data[4]
        p_population = row_data[5]

        if p_nta_code not in populationLookup:
            populationLookup[p_nta_code] = [p_population]
        else:
            populationLookup[p_nta_code].append(p_population)

with open('data/neighborhood-lookup.csv', newline='', encoding='utf-8') as lookup_file:
    lookupReader = csv.reader(lookup_file)

    with open('data/neighborhood-lookup-plus-pop.csv', 'w', newline='', encoding='utf-8') as out_file:
        csvWriter = csv.writer(out_file)

        header = True
        for row_data in lookupReader:
            if header:
                csvWriter.writerow(row_data + ["l_pop_2000", "l_pop_2010"])
                header = False
                continue
            
            l_nta_id = row_data[6]
            csvWriter.writerow(row_data + populationLookup[l_nta_id])
