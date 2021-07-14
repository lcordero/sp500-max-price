# Python v3.8.5

import requests
import configparser

# API call limits - Basic Subscription
# - 500 requests per month
# - 5 requests per second
# Expected number of call ~132 per month

parser = configparser.ConfigParser()
parser.read("./config.local")

# Request information
requestHeaders = {
    'x-rapidapi-key': parser.get("api", "key"),
    'x-rapidapi-host': parser.get("api", "host")
    }

# MaxPrice information
maxPriceUrl = parser.get("api", "host") + "/stock/v3/get-historical-data"
maxPriceQueryStr = {"symbol":"MES=F","region":"US"}
maxPriceResponse = requests.request("GET", maxPriceUrl, headers=requestHeaders, params=maxPriceQueryStr)

# Current Volatility
volatilityUrl = parser.get("api", "host") + "/market/v2/get-quotes"
volatilityQueryStr = {"region":"US","symbols":"^VIX"}
volatilityResponse = requests.request("GET", volatilityUrl, headers=requestHeaders, params=volatilityQueryStr)


print(maxPriceResponse.text)

print(volatilityResponse.text)