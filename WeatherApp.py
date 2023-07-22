import requests
import json

city = input("Enter your city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}&aqi=no"
r = requests.get(url)
data = json.loads(r.text)  # Use json.loads() to parse the JSON data


print(data['current']['temp_c'])  # Access the 'temp_c' value under 'current' key
