#!/usr/bin/env python3

import requests 
import random 

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")

 #   for catfact in r.json()["all"]:
#        print(catfact.get("text"))
    listOfCatFacts = r.json()

    randomFact = random.choice(listOfCatFacts["all"])

    print(randomFact["text"])


    print(r.status_code)

main()
