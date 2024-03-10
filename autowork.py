import requests
import time
import random

with open("info.txt", "r") as file:
    info = file.read().splitlines()

def configure_info():
    try:
        token = input("Discord token: ")
        with open("info.txt", "w") as file:
            file.write(f"{token}")
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
    r = requests.post("https://discord.com/api/v9/channels/1212544929667092510/messages?limit=50", data=payload, headers=header)
    time.sleep(random.randrange(3,10))

def send_typing():
    r = requests.post("https://discord.com/api/v9/channels/1212544929667092510/typing", headers=header)
    time.sleep(random.randrange(1,2))

if len(info) == 0:
    configure_info()
    print("Successfully configured Discord token! Run autowork.py to start the bot.")
    exit()

messages = [".work", ".work", ".work", ".work", ".work", ".work", ".work", ".bet 5000", ".bet 10000" ".bal"]

header = {
    'authorization': info[0]
}

print("Auto work started! Press CTRL+C to stop.")

while 1 == 1:
    payload = {
        'content' : random.choice(messages)
    }
    send_typing()
    send_message()