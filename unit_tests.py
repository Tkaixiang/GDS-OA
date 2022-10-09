import pandas as pd
import sys

# Check restaurants.csv
presentColumns = ["Restaurant Id","Restaurant Name","Country","City","User Rating Votes","User Aggregate Rating","Cuisines"]
modelRestaurantData = {'Restaurant Id': 18649486, 'Restaurant Name': 'The Drunken Botanist', 'Country': 'India', 'City': 'Gurgaon', 'User Rating Votes': 4765, 'User Aggregate Rating': 4.4, 'Cuisines': 'Continental, Italian, North Indian, Chinese'}
restaurantData = pd.read_csv('restaurants.csv').to_dict('index')

firstRestaurant = restaurantData[0]

print("=====Checking restaurants.csv=====")
failed = False
# 1. Check that all columns are present
for column in presentColumns:
    if (column not in firstRestaurant):
        print("'" + column + "' is missing from the record")
        failed = True
        sys.exit(0)

for x in firstRestaurant:
    # 2. Check data values
    if (firstRestaurant[x] != modelRestaurantData[x]):
        print("Wrong data value \n Expected: '" + modelRestaurantData[x] + "' | Received: '" + firstRestaurant[x] + "'")
        failed = True

if (failed):
    print("restaurants.csv has failed the tests")
else:
    print("restaurants.csv has passed the tests")

print("=====Checking restaurant_events.csv=====")
# Check restaurant_events.csv
presentColumns = ["Event Id","Restaurant Id","Restaurant Name","Photo URL","Event Title","Event Start Date","Event End Date"]
modelRestaurantData = {'Event Id': 336644, 'Restaurant Id': 18856789, 'Restaurant Name': 'AIR- An Ivory Region', 'Photo URL': 'https://b.zmtcdn.com/data/zomato_events/photos/46f/1c1651fcd360fe1468cfc06125b1646f_1554705305.jpg', 'Event Title': 'Dhol Bhangra Night', 'Event Start Date': '2019-04-10', 'Event End Date': '2019-04-11'}
restaurantData = pd.read_csv('restaurant_events.csv').to_dict('index')


failed = False
firstRestaurant = restaurantData[0]

# 1. Check that all columns are present
for column in presentColumns:
    if (column not in firstRestaurant):
        print("'" + column + "' is missing from the record")
        failed = True
        sys.exit(0)

for x in firstRestaurant:
    # 2. Check data values
    if (firstRestaurant[x] != modelRestaurantData[x]):
        print("Wrong data value \n Expected: '" + modelRestaurantData[x] + "' | Received: '" + firstRestaurant[x] + "'")
        failed = True

if (failed):
    print("restaurants.csv has failed the tests")
else:
    print("restaurants.csv has passed the tests")