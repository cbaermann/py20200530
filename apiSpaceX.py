#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""
# python3 -m pip install requests
import requests


# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = requests.get(SPACEXURI)
    listOfCores = coreData.json()




    for core in listOfCores:
        print("Core Serial: " + str(core["core_serial"]), 
                "Launch Date: " +  str(core["original_launch"]), 
                "Missions: " + str(core["missions"]) ,  end="\n\n")
        


if __name__ == "__main__":
    main()
