import requests
import random
import string
import time
import os
from datetime import datetime
from faker import Faker
import webbrowser

fake = Faker()

print(f"Name: {fake.name()}")
print(f"Female: {fake.first_name_female()}", end=" ")
print(f"{fake.last_name_female()}")
print(f"Male: {fake.first_name_male()}", end=" ")
print(f"{fake.last_name_male()}\n")
print(f"Online Username: {fake.user_name()}\n")
print(f"Phone: {fake.basic_phone_number()}\n")
print(f"Address: {fake.address()}")
print(f"Country: {fake.country()}\n")
print(f"Date: {fake.date(pattern='%A, %B, %d/%m/%Y')}\n")
print(f"License Plate: {fake.license_plate()}\n")
print(f"Latitude: {fake.latitude()}", f"Longitude: {fake.longitude()}\n")

BASE_URL = "https://api.mail.tm"

# Generate random username
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# Get available domains
domains = requests.get(f"{BASE_URL}/domains").json()
domain = domains["hydra:member"][0]["domain"]

email = f"{username}@{domain}"
password = "StrongPass123"

print("Email:", email)

# Create account
requests.post(f"{BASE_URL}/accounts", json={"address": email, "password": password})

# Login
token = requests.post(f"{BASE_URL}/token", json={"address": email, "password": password}).json()["token"]

headers = {"Authorization": f"Bearer {token}"}

seen_ids = set()

print("Waiting for emails...\n")

while True:
    messages = requests.get(f"{BASE_URL}/messages", headers=headers).json()
    mails = messages["hydra:member"]

    for mail in mails:
        if mail["id"] not in seen_ids:
            seen_ids.add(mail["id"])

            # Fetch full mail detail (contains HTML body)
            detail = requests.get(f"{BASE_URL}/messages/{mail['id']}", headers=headers).json()

            html_parts = detail.get("html", [])
            html_body = html_parts[0] if html_parts else f"<pre>{detail.get('text', '')}</pre>"

            # Save HTML to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"{os.getcwd()}"

            with open(f"{filepath}/mail.html", "w") as f:
                f.write(html_body)

            print(f"New mail from: {detail['from']['address']}")
            print(f"Subject: {detail['subject']}")

            webbrowser.open(f"file://{os.getcwd()}/mail.html")


    time.sleep(5)