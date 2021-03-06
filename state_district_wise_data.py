# Date State District Wise API Data
# url: "https://api.covid19india.org/state_district_wise.json"
# Importing data from above url to python variable.
# Author: Varun S Kulkarni, Praveenkumar A, Shivkumara K

import urllib.request as request
import json
from create_csv_file import CreateCSVFile

class CovidstateDistrictWiseData(CreateCSVFile):
    def __init__(self, url="https://api.covid19india.org/state_district_wise.json"):
        with request.urlopen(url) as req:
            if req.getcode() == 200:
                self.src = req.read()
                self.json_data = json.loads(self.src)
                self.states = states = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Delhi","Dadra and Nagar Haveli and Daman and Diu","Goa","Gujarat","Himachal Pradesh"
                                        ,"Haryana","Jharkhand","Jammu and Kashmir","Karnataka","Kerala","Ladakh","Lakshadweep","Maharashtra","Meghalaya","Manipur","Madhya Pradesh","Mizoram","Nagaland","Odisha","Punjab","Puducherry","Rajasthan","Sikkim"
                                        ,"Telangana","Tamil Nadu","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
                self.state_district_data = self.generate_state_district_key_value_pair(self.json_data, self.states)
                self.fields = ["District", "Active", "Confirmed", "Deceased", "Recovered"]
                self.rows = list()
                for state in self.states:
                    self.rows = []
                    for district in self.state_district_data[state]:
                        temp = []
                        temp.append(district)
                        temp.append(self.state_district_data[state][district]["active"])
                        temp.append(self.state_district_data[state][district]["confirmed"])
                        temp.append(self.state_district_data[state][district]["deceased"])
                        temp.append(self.state_district_data[state][district]["recovered"])
                        self.rows.append(temp)                        
                    obj = CreateCSVFile("D:/7_8_SEM_PROJECT/Code/state_district/"+state+".csv",self.fields, self.rows)                
            else:
                print("!Error occoured while reading data from an API")

    def generate_state_district_key_value_pair(self, json_data, states):
        key_value = dict()        
        for state in states:
            key_value[state] = json_data[state]["districtData"]
        # print(key_value)
        return key_value


obj = CovidstateDistrictWiseData()