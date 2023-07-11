import requests
import time


def main():
  wile True:
    req = requests.get()
    print(req.json)
    time.sleep(15)
