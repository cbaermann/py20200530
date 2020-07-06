#!/usr/bin/python3

import requests

IPURL = "http://ip.jsontest.com/"

def main():
    response = requests.get(IPURL)

    json_response = response.json()

    print(json_response)


    print(f"The current WAN IP is ---> {json_response['ip']}")


if __name__ == "__main__":
    main()
