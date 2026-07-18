
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt 

API_KEY = "Enter_ your_api_key"


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

states = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

weather_list = []



for state, city in states.items():

    # API URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    print("\nAPI URL :")
    print(url)

    # GET REQUEST
    response = requests.get(url)

    # STATUS CODE
    print("Status Code :", response.status_code)

    # SUCCESS
    if response.status_code == 200:

        data = response.json()

        weather_data = {
            "State": state,
            "Capital": city,
            "Temperature": data["main"]["temp"],
            "Feels_Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Weather": data["weather"][0]["description"],
            "Wind_Speed": data["wind"]["speed"],
            "Clouds": data["clouds"]["all"],
            "Visibility": data.get("visibility", "N/A")
        }

        weather_list.append(weather_data)

        print("Data Fetched Successfully")

    else:

        print("API Error")
        print(response.json())

    # Delay
    time.sleep(1)

df = pd.DataFrame(weather_list)


df.to_csv("india_weather_data.csv", index=False)



print("\nComplete Weather Data")
print(df)

print("\nCSV File Saved Successfully")
df.plot(
    x="State",
    y=["Temperature", "Feels_Like"],
    kind="bar",
    figsize=(16, 7)
)


plt.title("Temperature and Feels Like")
plt.xlabel("State")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=90)
plt.show()
