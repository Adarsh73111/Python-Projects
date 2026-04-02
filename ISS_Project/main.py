# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# GMT
# import requests
# from datetime import datetime
# my_lat = 30.35433
# my_lng = 76.36973
# parameters = {
#     "lat": my_lat,
#     "lng": my_lng,
#     "formatted": 0,
# }
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
# print(sunrise.split("T")[1].split("+")[0])
# print(sunset.split("T")[1].split("+")[0])
# time_now = datetime.now()
# print(time_now.strftime("%Y-%m-%dT%I:%M:%S %p").split("T")[1])

# IST
import requests
from datetime import datetime, timedelta
my_lat = 30.35433
my_lng = 76.36973
parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_utc = datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S+00:00")
sunset_utc = datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S+00:00")

sunrise_ist = sunrise_utc + timedelta(hours=5, minutes=30)
sunset_ist = sunset_utc + timedelta(hours=5, minutes=30)

print("Sunrise (IST):", sunrise_ist.strftime("%I:%M:%S %p"))
print("Sunset  (IST):", sunset_ist.strftime("%I:%M:%S %p"))

time_now = datetime.now()
print("Current (IST):", time_now.strftime("%I:%M:%S %p"))