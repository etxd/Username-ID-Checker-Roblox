import requests
import time

usernames = []
with open('usernames.txt', 'r') as file:
    usernames = file.read().splitlines()

API_ENDPOINT = "https://users.roblox.com/v1/usernames/users"

def getUserId(username):
    requestPayload = {
        "usernames": [username],
        "excludeBannedUsers": False
    }

    responseData = requests.post(API_ENDPOINT, json=requestPayload)

    if responseData.status_code == 200:
        data = responseData.json()["data"]
        if data:
            userId = data[0]["id"]
            result = f"{userId} - {username}"
            print(result)

            with open("output.txt", "a") as output_file:
                output_file.write(result + "\n")

            return userId
        else:
            print(f"Username not found: {username}")
    else:
        print(f"Error processing {username}. Status code: {responseData.status_code}")

    return None

for username in usernames:
    getUserId(username)
    time.sleep(0.1)