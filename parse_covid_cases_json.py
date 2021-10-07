import json
import csv

JSON_FILE_PATH = './covid_cases.json' # Path to JSON file.
with open(JSON_FILE_PATH) as infile:
    covid_cases = json.loads(infile.read()) # Load the JSON file.

CSV_FILE_PATH = './covid_cases_(fromJSON).csv' # CSV file path.
with open(CSV_FILE_PATH, 'w') as outfile:
    file = csv.writer(outfile)
    #  Set column names to dateRep, countriesAndTerritories, cases, and deaths.
    file.writerow(["dateRep", "countriesAndTerritories", "cases", "deaths"])
    
    # Write the entries for each column by iterating through each record.
    for record in covid_cases["records"]:
       file.writerow([
           record["dateRep"],
           record["countriesAndTerritories"],
           record["cases"],
           record["deaths"]
           ])


    