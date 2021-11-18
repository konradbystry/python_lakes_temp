from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
import requests as req
import json
import geocoder

api_url = 'https://nominatim.openstreetmap.org/search'
format = 'geojson' 

def fetch(region, station, water_body):
    res = req.get(api_url + '?q=Polska%' + region + '%' + station + '%' + water_body + '&format=' + format)
    print(api_url + '?q=Polska%' + region + '%' + station + '%' + water_body + '&format=' + format)
    return res.json()
    
#read xlsx data

lakes = pd.read_excel('water_temp_from_IMGW-PIB.xlsx')

for index, row in lakes.iterrows():
      #print(row['No'], row['region'], row['station'].replace(' ', '+'), row['water_body'])
      res_json = fetch(row['region'], row['station'].replace(' ', '+'), 'Gardno')
      print(res_json)
      row['coordinates'] = res_json.features.0.geometry.coordinates
    

# res_json = fetch('warmińsko-mazurskie', 'Ełk', 'Ełckie')
# print(res_json)