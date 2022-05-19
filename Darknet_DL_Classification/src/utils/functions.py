# import necessary libraries
import os

# create directory if directory not exists
def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)

#create fucntion to verify data path
def verify_existence_data(path):
    if os.path.isfile(path):
        return True
    return False

# create function to split ip data
def createGrams(ip: str) -> str:
    parts = ip.split('.')
    one_gram = parts[0]
    two_gram = f"{parts[0]} {parts[1]}"
    three_gram = f"{parts[0]} {parts[1]} {parts[2]}"
    return one_gram, two_gram, three_gram

# return ip details
def getIpsDetais(ip, ip_dict, repeated, ipinfo_handler):
    if ip not in ip_dict.keys():
        details = ipinfo_handler

# delete unnecessary space characters from data 
def deleteSpaces(arr):
    new_arr = [item.replace(" ", "_") for item in arr]
    return new_arr