# This file detects when the doorbell has been rung and send a notificaition
# to my phone.

import RPi.GPIO as GPIO
import time
import requests
import os
import json
import datetime


# GPIO SETUP
CHANNEL = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.IN)


def read_config() -> dict:
    filename = os.path.join("code/config.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


config = read_config()


def pushbullet_notification(title: str, body: str, TOKEN: str) -> requests.post:
    """
    Send a Pushbullet notification to my phone.

    """

    msg = {"type": "note", "title": title, "body": body}

    resp = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        data=json.dumps(msg),
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json",
        },
    )

    if resp.status_code != 200:
        raise Exception("Error", resp.status_code)
    else:
        pass


def doorbell_notfication(config):
    now = datetime.datetime.now()
    print("Sound Detected! - Sending notification")

    TOKEN = config["TOKEN"]
    pushbullet_notification(
        "Doorbell!",
        f'There is somebody at the door - {now.strftime("%Y-%m-%d %H:%M:%S")}',
        TOKEN,
    )


def doorbell_callback(channel):
    """
    Initialising the GPIO callback to send a text message when a
    sound is detected.

    """
    if GPIO.input(CHANNEL):
        doorbell_notfication(config)
        time.sleep(600)
    else:
        doorbell_notfication(config)
        time.sleep(600)


def main():
    GPIO.add_event_detect(CHANNEL, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(CHANNEL, doorbell_callback)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
