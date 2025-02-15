# Read rows starting from row 5 and extract column 1 (rank) and column 4 (institution name)
# Create a dictionary where the key is the university name and the value is its rank

import csv
import pycountry_convert as pc
from collections import defaultdict

def get_university_ranking_dict():
    # Initialize the dictionary to store university rankings
    university_ranking_dict = {}

    # Read the CSV file
    with open('/Users/oscar.huang.-nd/github/CitationMap/demo/ranking.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the first 4 rows (headers and irrelevant information)
        for _ in range(4):
            next(csv_reader)
        
        # Read relevant rows and construct the dictionary
        for row in csv_reader:
            if len(row) >= 4:
                rank = row[0].strip()
                university_name = row[3].strip()
                # Add to dictionary
                if rank and university_name:
                    university_ranking_dict[university_name] = rank
    
    return university_ranking_dict

def get_citation_affiliation_rank_list():
    university_ranking_dict = get_university_ranking_dict()
    affiliation_list = set()
    citers = set()
    with open('/Users/oscar.huang.-nd/github/CitationMap/demo/citation_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the first 4 rows (headers and irrelevant information)
        for _ in range(4):
            next(csv_reader)
        
        # Read relevant rows and construct the dictionary
        for row in csv_reader:
            if len(row) >= 5:
                affilation = row[4].strip()
                if row[1] not in citers:
                    citers.add(row[1])
                    affiliation_list.add((affilation, university_ranking_dict.get(affilation, '10000')))
        top50 = [item for item in affiliation_list if int(item[1]) < 50]
        top100 = [item for item in affiliation_list if int(item[1]) < 100]
        top500 = [item for item in affiliation_list if int(item[1]) < 500]
        top1000 = [item for item in affiliation_list if int(item[1]) < 1000]
        print(len(affiliation_list), len(top50), len(top50)/len(affiliation_list), 
              len(top100), len(top100)/len(affiliation_list), 
              len(top500), len(top500)/len(affiliation_list),
              len(top1000), len(top1000)/len(affiliation_list))

def get_citation_cities_countries():
    cities, countries = set(), set()
    with open('/Users/oscar.huang.-nd/github/CitationMap/demo/citation_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the first 4 rows (headers and irrelevant information)
        for _ in range(4):
            next(csv_reader)
        
        # Read relevant rows and construct the dictionary
        for row in csv_reader:
            if len(row) >= 11:
                county, city, state, country = row[7].strip(), row[8].strip(), row[9].strip(), row[10].strip()
                if len(city) > 0:
                    cities.add(city)
                elif len(county) > 0:
                    cities.add(county)
                elif len(state) > 0:
                    cities.add(state)
                
                countries.add(country)
    
    print(len(cities), len(countries))
    continent2country = defaultdict(list)
    for country in countries:
        continent = get_continent(country)
        if continent == 'Continent not found':
            continue
        continent2country[continent].append(country)
    for continent, countries in continent2country.items():
        countries.sort()
        print(continent, ', '.join(countries))

def get_continent(country_name):
    """Gets the continent of a given country."""

    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return "Continent not found"


if __name__ == "__main__":
    # get_citation_affiliation_rank_list()
    get_citation_cities_countries()
