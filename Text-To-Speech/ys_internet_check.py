# ys_internet_check.py

from time import sleep,time
from subprocess import call
import random
import requests

SITES = ["https://www.google.com","https://www.ibm.com"]
SLEEP = 2  # 20
REPORT_EXCEPTION = False

def getUrl():
    return random.choice(SITES)

def internet_check():
    try:
        _ = requests.get(getUrl(),timeout=5)
        return True, None
    except Exception as e:
        return False, e

if __name__ == "__main__":
    t = time()
    count= 0
    while True:
        print(f"{time() - t:.2f}", end=' ', flush=True)
        check, e = internet_check()
        if check:
            message = "Internet is connected!"
            call(["espeak", "-v", "en", message])
            print(message)
        else:
            count+=1
            if count>=3:
                message = "Internet is down"
                call(["espeak", "-v", "en", message])
                print(message)
                count=0
            if REPORT_EXCEPTION:
                print(f"Error: {e}")
        sleep(SLEEP)
