# Date Wise API Data
# url: "https://api.covid19india.org/data.json"
# Importing data from above url to python variable.
# Author: Varun S Kulkarni, Praveenkumar A, Shivkumara K.

import urllib.request as request
import json
from create_csv_file import CreateCSVFile

class CovidDateWiseData(CreateCSVFile):
    def __init__(self, url="https://api.covid19india.org/data.json"):
        with request.urlopen(url) as req:
            if req.getcode() == 200:
                self.src = req.read()
                self.json_data = json.loads(self.src)
                self.date_data = self.generate_date_key_value_pair(self.json_data)
                self.no_data = self.generate_no_key_value_pair(self.json_data)
                self.fields = ["DailyConfirmed", "DailyDeceased", "DailyRecovered"]
                self.rows = self.return_csv_rows(self.no_data)
                self.fileName = "date_wise_data.csv"
                obj = CreateCSVFile("D:/7_8_SEM_PROJECT/Code/date/"+self.fileName, self.fields, self.rows)
            else:
                print("!Error occoured while reading data from an API")

    def generate_date_key_value_pair(self, json_data):
        key_value = dict()
        no_of_days = len(json_data["cases_time_series"])
        for n in range(0, no_of_days):
            key_value[json_data["cases_time_series"][n]["dateymd"]] = json_data["cases_time_series"][n]
        # Retrive data -- (Shown Below)
        # print(key_value["2020-01-30"]["dailyconfirmed"])        
        return key_value

    def generate_no_key_value_pair(self, json_data):
        key_value = dict()
        no_of_days = len(json_data["cases_time_series"])
        for n in range(0, no_of_days):
            key_value[n] = json_data["cases_time_series"][n]
        # Retrive data -- (Shown Below)
        # print(key_value[0]["dailyconfirmed"])
        return key_value
    
    def return_csv_rows(self, key_value):
        rows = list()
        for i in range(0, len(key_value)):
            temp = []
            temp.append(key_value[i]["dailyconfirmed"])
            temp.append(key_value[i]["dailydeceased"])
            temp.append(key_value[i]["dailyrecovered"])
            rows.append(temp)        
        return rows

obj = CovidDateWiseData()