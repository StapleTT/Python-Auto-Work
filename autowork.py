import requests
import time
import random

with open("info.txt", "r") as file:
    info = file.read().splitlines()

def configure_info():
    try:
        token = input("Discord token: ")
        channel_id = input("Channel ID: ")
        with open("info.txt", "w") as file:
            file.write(f"{token}\n{channel_id}")
    except Exception as e:
        print(f"Error configuring Discord token{e}")
        exit()

def set_channel():
    token = info[0]
    with open("info.txt", "w") as file:
        file.write(f"{token}")

def send_message():
    global choice
    choice = random.choice(messages)
    r = requests.post("https://discord.com/api/v9/channels/" + info[1] + "/messages?limit=50", data=payload, headers=header)
    time.sleep(random.randrange(2,5))

def send_typing():
    r = requests.post("https://discord.com/api/v9/channels/" + info[1] + "/typing", headers=header)
    time.sleep(random.randrange(1,2))

if (len(info) == 0):
    print("Missing configuration files! Attempting to reconfigure...")
    time.sleep(2)
    configure_info()
    print("Successfully configured! Run autowork.py again to start the bot.")
    exit()

messages = [".work", ".work", ".work", ".work", ".work", ".work", ".work", ".bet 5000"]
messages2 = [".work", ".work", ".work", ".work", ".work", ".work", ".work", ".bet 5000", ".bet 10000", ".bal"]

header = {
    'authorization': info[0]
}

print("Auto work started! Press CTRL+C to stop.")

last_message = ".work"

while 1 == 1:
    if("bet" or "bal" in last_message):
        last_message = random.choice(messages)
    else:
        last_message = random.choice(messages2)
    payload = {
    'content' : last_message
    }
    send_typing()
    send_message()