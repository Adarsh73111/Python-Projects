# Cloud Code for ISS
import requests
import math
import smtplib
import time
from datetime import datetime, timezone, timedelta

MY_LAT = 30.35433
MY_LONG = 76.36973
MY_EMAIL = "workonprojects24@gmail.com"
MY_PASSWORD = ""
RADAR_RANGE_KM = 500

email_sent_for_current_pass = False


def get_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


def send_radar_alert(distance):
    try:
        utc_now = datetime.now(timezone.utc)
        ist_now = utc_now + timedelta(hours=5, minutes=30)
        current_time = ist_now.strftime("%I:%M %p")

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:RADAR ALERT: ISS Approaching!\n\nThe ISS is currently {int(distance)} km away from Patiala.\nTime: {current_time} (IST)\n\nLook up!"
        )
        connection.close()
    except Exception:
        pass


while True:
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        lat = float(data["iss_position"]["latitude"])
        lng = float(data["iss_position"]["longitude"])

        dist = get_distance(MY_LAT, MY_LONG, lat, lng)

        if dist <= RADAR_RANGE_KM:
            if not email_sent_for_current_pass:
                send_radar_alert(dist)
                email_sent_for_current_pass = True
        else:
            if dist > RADAR_RANGE_KM + 100:
                email_sent_for_current_pass = False

    except Exception:
        pass

    time.sleep(60)