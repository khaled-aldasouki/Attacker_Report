#/bin/python3

"""
Khaled Aldasouki
3-5-2023
Please note that the script cannot be executed because it was written on a windows machine, and the text formatting is causing errors
however the script can still be run using the Python interpretor or an IDE
"""

from collections import Counter
import re
import requests 
import os
from sys import platform
import time
"""
Method to find the location of an ip address using ipapi api requests
"""
def get_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        return response.get('country_code')
    except:
        os.system("clear")
        print("An error has occured while trying to get the IP location. Please make sure you are connected to the internet before running the script.")
        exit(-1)
"""
reads the log file and organizes the ip addresses and their attempt counts into a dictionary
"""
def get_report(logFile):
    if logFile.strip() == "":
        logFile = "/var/log/syslog"
    if os.path.exists(logFile):
        print(f'Reporting "{logFile}":')

        with open(logFile) as file:
            f = file.read()
            dic = dict()
            failed = re.findall("Failed .* [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} port",f)
            for fail in failed: 
                ip = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", fail)[0]
                if ip in dic:
                    dic[ip] += 1
                else:
                    dic[ip] = 1
        sorted_dic = dict(sorted(dic.items(), key=lambda x:x[1]))
        return sorted_dic
    
    else:
        print(f"File {logFile} does not exist.")
        


"""
Takes in a dictionary of ip addresses and their attempts, gets the location, then prints it in a formatted way
"""
def print_report(sorted_dic):
    print(f'\033[0;31m{"Attempts":8}  {"IP":16}  {"Country":9}\033[0m')

    for ip in sorted_dic:
        location = None
        while location == None:
            location = get_location(ip)

        
        print(f"{str(sorted_dic[ip]).ljust(8)}  {ip:16}  {location:9}")
    
    
def main():
    os.system("clear")
    if platform == "win32":
        print("This tool is made for Linux and cannot be used on Windows.")
        time.sleep(5)

    elif (report := get_report(input("Please enter the log file you'd like to get a report on: "))) != None:
        print_report(report)
        time.sleep(5)

if __name__ == "__main__":
    main()

