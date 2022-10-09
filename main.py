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


restaurantCSVData = {
    "Restaurant Id": [],
    "Restaurant Name": [],
    "Country": [],
    "City": [],
    "User Rating Votes": [],
    "User Aggregate Rating": [],
    "Cuisines": []
}
restaurantEventsCSVData = {
    "Event Id": [],
    "Restaurant Id": [],
    "Restaurant Name": [],
    "Photo URL": [],
    "Event Title": [],
    "Event Start Date": [],
    "Event End Date": []
}

ratingThresholds =  {
    "Excellent": {'max': 0, 'min': 999},
    "Very Good": {'max': 0, 'min': 999},
    "Good": {'max': 0, 'min': 999},
    "Average": {'max': 0, 'min': 999},
    "Poor": {'max': 0, 'min': 999}
}

for data in jsonData:
    mainRestaurantData = data['restaurants']


    for x in mainRestaurantData:
        # TASK 1: Extract the following fields and store the data as restaurants.csv
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

        # TASK 2: Extract the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv
        if ("zomato_events" in currentResObj):

            currentEvents = currentResObj["zomato_events"]
            for event in currentEvents:
                mainEventObj = event["event"]

                startDate = mainEventObj["start_date"]
                endDate = mainEventObj["end_date"]

                # Only if in the month of April 2019
                if (startDate[:7] == "2019-04" or endDate[:7] == "2019-04"):
                    restaurantEventsCSVData["Event Id"].append(mainEventObj["event_id"])
                    restaurantEventsCSVData["Restaurant Id"].append(currentResObj["R"]["res_id"])
                    restaurantEventsCSVData["Restaurant Name"].append(currentResObj['name'])

                    photoList = mainEventObj["photos"]
                    if (len(photoList) > 0):
                        restaurantEventsCSVData["Photo URL"].append(photoList[0]["photo"]["url"])
                    else:
                        restaurantEventsCSVData["Photo URL"].append("NA")
                    
                    restaurantEventsCSVData["Event Title"].append(mainEventObj["title"])
                    restaurantEventsCSVData["Event Start Date"].append(startDate)
                    restaurantEventsCSVData["Event End Date"].append(endDate)
        
        # TASK 3: From the dataset (restaurant_data.json), determine the threshold for the different rating text based on aggregate rating. Return aggregates for the following ratings only:
        

pd.DataFrame.from_dict(restaurantCSVData).to_csv('restaurants.csv', index=False)
pd.DataFrame.from_dict(restaurantEventsCSVData).to_csv('restaurants_events.csv', index=False)
