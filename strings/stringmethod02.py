#!/usr/bin/env python3


def main():
    """ Run-time code"""

    lilstring = "Alta4 Reasearch offers classes on Python coding"
    newlist = lilstring.split(" ")

    print(newlist)

    myiplist = ["192", "168", "0", "12"]

    singleip = ".".join(myiplist)

    print(singleip)


main()
