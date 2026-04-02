# Advance Version
import turtle
import requests
import math
import smtplib
import datetime

# --- Configuration ---
MY_LAT = 30.35433
MY_LONG = 76.36973
MY_EMAIL = "workonprojects24@gmail.com"
MY_PASSWORD = "fhbn mcft dfyo fhxu"  # Put your App Password here
RADAR_RANGE_KM = 500  # The "Radar" notification distance

# --- State Variable to prevent email spam ---
# False = We haven't sent an email for this pass yet.
# True = We already alerted the user for this pass.
email_sent_for_current_pass = False


def get_distance(lat1, lon1, lat2, lon2):
    """Calculates distance between two points on Earth using Haversine formula"""
    R = 6371  # Earth radius in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


def send_radar_alert(distance):
    """Sends the email notification"""
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("RADAR ALERT: Sending Email...")

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:RADAR ALERT: ISS Approaching!\n\nThe ISS is currently {int(distance)} km away from Patiala.\nTime: {current_time}\n\nLook up!"
        )
        connection.close()
        print("Email Sent Successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# --- GUI Setup ---
screen = turtle.Screen()
screen.title("ISS Radar System - Patiala Sector")
screen.setup(width=720, height=360)

try:
    screen.bgpic("world_map.gif")
except:
    pass

screen.setworldcoordinates(-180, -90, 180, 90)

# ISS Object
iss = turtle.Turtle()
iss.shape("circle")
iss.color("red")
iss.penup()

# Patiala Base Station Object
patiala = turtle.Turtle()
patiala.penup()
patiala.hideturtle()
patiala.color("blue")
patiala.goto(MY_LONG, MY_LAT)
patiala.dot(5)
patiala.write(" Patiala (Base)", font=("Arial", 10, "bold"))

# Range Circle (Visualizing the 200km zone - roughly)
# Note: On a flat map projection, a perfect circle is distorted,
# but this gives a visual target.
range_ring = turtle.Turtle()
range_ring.penup()
range_ring.color("green")
range_ring.goto(MY_LONG, MY_LAT - 2)  # Offset slightly
range_ring.pendown()
range_ring.circle(2)  # Draw a small visual circle around Patiala
range_ring.hideturtle()


def track_iss():
    global email_sent_for_current_pass

    try:
        # 1. Fetch Data
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        lat = float(data["iss_position"]["latitude"])
        lng = float(data["iss_position"]["longitude"])

        # 2. Update Visuals
        iss.goto(lng, lat)

        # 3. Calculate Distance
        dist = get_distance(MY_LAT, MY_LONG, lat, lng)

        # 4. Radar Logic
        status_msg = ""

        if dist <= RADAR_RANGE_KM:
            # ISS is INSIDE the zone
            iss.color("green")  # Change color to indicate "Lock"
            status_msg = "TARGET LOCKED - IN RANGE"

            # Only send email if we haven't sent one for this specific pass yet
            if not email_sent_for_current_pass:
                send_radar_alert(dist)
                email_sent_for_current_pass = True
        else:
            # ISS is OUTSIDE the zone
            iss.color("red")
            status_msg = "SCANNING..."

            # Reset the trigger so it works again next orbit
            if dist > RADAR_RANGE_KM + 50:  # Add buffer to prevent flickering
                email_sent_for_current_pass = False

        # 5. Update Screen Text
        screen.title(f"RADAR: {status_msg} | Dist: {int(dist)} km")
        print(f"ISS: {lat}, {lng} | Dist: {int(dist)} km | Alert Sent: {email_sent_for_current_pass}")

    except Exception as e:
        print(f"Error: {e}")

    # Run this function again in 5000ms (5 seconds)
    screen.ontimer(track_iss, 5000)


# --- Start ---
track_iss()
screen.mainloop()

# Cloud Code for ISS
# import requests
# import math
# import smtplib
# import time
# from datetime import datetime, timezone, timedelta
#
# MY_LAT = 30.35433
# MY_LONG = 76.36973
# MY_EMAIL = "workonprojects24@gmail.com"
# MY_PASSWORD = ""
# RADAR_RANGE_KM = 500
#
# email_sent_for_current_pass = False
#
#
# def get_distance(lat1, lon1, lat2, lon2):
#     R = 6371
#     dLat = math.radians(lat2 - lat1)
#     dLon = math.radians(lon2 - lon1)
#     a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
#         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
#         math.sin(dLon / 2) * math.sin(dLon / 2)
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     d = R * c
#     return d
#
#
# def send_radar_alert(distance):
#     try:
#         utc_now = datetime.now(timezone.utc)
#         ist_now = utc_now + timedelta(hours=5, minutes=30)
#         current_time = ist_now.strftime("%I:%M %p")
#
#         connection = smtplib.SMTP("smtp.gmail.com", 587)
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:RADAR ALERT: ISS Approaching!\n\nThe ISS is currently {int(distance)} km away from Patiala.\nTime: {current_time} (IST)\n\nLook up!"
#         )
#         connection.close()
#     except Exception:
#         pass
#
#
# while True:
#     try:
#         response = requests.get(url="http://api.open-notify.org/iss-now.json")
#         response.raise_for_status()
#         data = response.json()
#
#         lat = float(data["iss_position"]["latitude"])
#         lng = float(data["iss_position"]["longitude"])
#
#         dist = get_distance(MY_LAT, MY_LONG, lat, lng)
#
#         if dist <= RADAR_RANGE_KM:
#             if not email_sent_for_current_pass:
#                 send_radar_alert(dist)
#                 email_sent_for_current_pass = True
#         else:
#             if dist > RADAR_RANGE_KM + 100:
#                 email_sent_for_current_pass = False
#
#     except Exception:
#         pass
#
#     time.sleep(60)