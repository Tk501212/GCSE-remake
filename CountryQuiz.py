import requests , random

response = requests.get("https://api.sampleapis.com/countries/countries")
data = response.json()


randomCountry = random.choice(data)

print(randomCountry["name"])

print("what is the capital city of" , randomCountry["name"])

answer = input("Capital: ")

if answer == randomCountry["capital"]:
    print("well done!")
else: 
    print("wrong...")
    print(randomCountry["capital"])


