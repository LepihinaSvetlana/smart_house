import requests
import time


def main():
  while True:
    req = requests.get()
    print(req.json)
    time.sleep(15)
