# from flask import Flask, request, jsonify
# import requests
# from tabulate import tabulate  # for neat table printing

# 1. Fetch data from a URL
import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    # 1. GET request to the URL
    with urllib.request.urlopen(url) as response:
        if response.status != 200:
            print(f"❌ Failed to fetch data. Status code: {response.status}")
            exit()
        data = response.read().decode("utf-8")

    # 2. Parse JSON response
    users = json.loads(data)

    if not users:
        print("⚠️ No users found.")
        exit()

    # 3. Optional: filter only users whose city starts with 'S'
    filter_by_city_S = input("Filter users whose city starts with 'S'? (y/n): ").lower() == "y"
    if filter_by_city_S:
        users = [u for u in users if u.get("address", {}).get("city", "").startswith("S")]

    # 4. Display user details
    print("\n================== USER LIST ==================\n")
    for i, user in enumerate(users, start=1):
        name = user.get("name", "N/A")
        username = user.get("username", "N/A")
        email = user.get("email", "N/A")
        city = user.get("address", {}).get("city", "N/A")

        print(f"User {i}:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print("-" * 40)

    print("\n✅ Done.")

except Exception as e:
    print("❌ Error occurred while fetching or displaying data:", e)
