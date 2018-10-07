#!/usr/bin/python
import os
import urllib2
import json


def style():
    print "\033[97m     ___          __  _  __   _____  _  "
    print "\033[97m    / | \        / / | | \ \ |  __ \| | "
    print "\033[97m   | | \ \  /\  / /__| |__| || |  | | |_ _   __ _  __ _ _ __"
    print "\033[97m  / /   \ \/  \/ / _ \ '_ \\ \ |  | | '_ \ / _` |/ _` | '__|"
    print "\033[97m  \ \    \  /\  /  __/ |_) / / |__| | | | | (_| | (_| | | "
    print "\033[97m   | |    \/  \/ \___|_.__/ ||_____/|_| |_|\__,_|\__,_|_|"
    print "\033[97m    \_\                  /_/        "
    print "\033[93m         IP Finder Tool   \n"

def sub():

    while True:
        ip = raw_input("\033[93m IP Address: ")
        url = "http://ip-api.com/json/"
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)



        style()

        print("\033[93m" + "\n IP: " + values['query'])
        print("\033[93m" + " Status: " + values['status'])
        print("\033[93m" + " Region: " + values['regionName'])
        print("\033[93m" + " Country: " + values['country'])
        print("\033[93m" + " City: " + values['city'])
        print("\033[93m" + " Internet Service Provider: " + values['isp'])
        print("\033[93m" + " Latitude,Longitude: " + str(values['lat']) + "," + str(values['lon']))
        print("\033[93m" + " ZIPCODE: " + values['zip'])
        print("\033[93m" + " Time Zone: " + values['timezone'])
        print("\033[93m" + " AS: " + values['as'] + "\n")
        break

style()
sub()




