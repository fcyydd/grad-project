# import necessary libraries

import ipinfo
import json
from tqdm import tqdm

# create a class 
class CatIPInformation:
    # defining variables
    def __init__(self, handler, _ips):
        self.handler = ipinfo.getHandler(handler)
        self.ips = _ips
        self.ip_dict = self.loadIps('Dataset/ips_dict.json')

        for i in tqdm(range(len(self.ips))):
            self.getIPDetail(self.ips[i])

        self.dumpIps('Dataset/ips_dict')

    # create function to load ips
    def loadIps(self, file):
        data = {}
        with open(file) as json_file:
            data = json.load(json_file)
        return data

    # create function to write ips to json file
    def dumpIps(self, folder):
        j = json.dumps(self.ip_dict)
        f = open(f'{folder}ips_dict.json', "w")
        f.write(j)
        f.close()

    # create a function to 
    def getIPDetail(self, ip):
        self.repeated = 0
        if ip not in self.ip_dict.keys():
            details = self.handler.getDetails(ip)
            self.ip_dict[ip] = details.all
        else:
            self.repeated += 1

    # create a function to create a ip_dict pointer
    def getIpsDict(self) -> dict:
        return self.ip_dict
