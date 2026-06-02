import requests

api_key = "YOUR_API_KEY"
city = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

data = requests.get(url).json()

weather = data["weather"][0]["main"]

print("Weather:", weather)

if weather == "Rain":
    print("Congestion probability increased")
