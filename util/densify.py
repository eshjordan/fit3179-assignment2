#!/usr/bin/env python3
import csv

agg_file = r'./data/all-neighborhoods-data-apr14-new.csv'
out_file = r'./data/densified-pickups.csv'

with open(agg_file, newline='', encoding='utf-8') as csvf:
    csvReader = csv.reader(csvf)

    with open(out_file, 'w', newline='', encoding='utf-8') as outf:
        csvWriter = csv.writer(outf)

        csvWriter.writerow(['d_neighborhood', 'd_hour'])

        header = True
        for row_data in csvReader:
            if header:
                header = False
                continue

            neighborhood = row_data[0]

            for hour in range(24):
                count = int(row_data[hour+1])
                for i in range(count):
                    csvWriter.writerow([neighborhood, hour])
