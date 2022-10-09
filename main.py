# Initial commitit
import pandas as pd
import json

# Read files given
excelFileDictionary = pd.read_excel("Country-Code.xlsx").to_dict('records')
countryCodeMapping = {} # Create a mapping of countrycode -> Country
for record in excelFileDictionary:
    countryCodeMapping[record['Country Code']] = record['Country']

jsonData = {}
with open('restaurant_data.json', encoding='utf-8') as f:
    jsonData = json.load(f)

# TASK 1: Extract the following fields and store the data as restaurants.csv
restaurantCSVData = {
    "Restaurant Id": [],
    "Restaurant Name": [],
    "Country": [],
    "City": [],
    "User Rating Votes": [],
    "User Aggregate Rating": [],
    "Cuisines": []
}
for data in jsonData:
    mainRestaurantData = data['restaurants']


    for x in mainRestaurantData:
        currentResObj = x["restaurant"]
        restaurantCSVData["Restaurant Id"].append(currentResObj["R"]["res_id"]) # Resurant ID
        restaurantCSVData["Restaurant Name"].append(currentResObj['name']) # Name

        # Some country codes don't exist in the xlsx
        countryID = currentResObj["location"]["country_id"]
        if (countryID in countryCodeMapping):
            restaurantCSVData["Country"].append(countryCodeMapping[countryID])
        else:  restaurantCSVData["Country"].append("Unknown Country Code")
        restaurantCSVData["City"].append(currentResObj["location"]["city"])
        restaurantCSVData["User Rating Votes"].append(currentResObj["user_rating"]["votes"])
        restaurantCSVData["User Aggregate Rating"].append(float(currentResObj["user_rating"]["aggregate_rating"]))
        restaurantCSVData["Cuisines"].append(currentResObj["cuisines"])

resCSVPD = pd.DataFrame.from_dict(restaurantCSVData)
resCSVPD.to_csv('restaurants.csv', index=False)
