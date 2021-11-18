import requests as req
import json

class Geocoder:
    
    api_url = 'https://nominatim.openstreetmap.org/search'
    format = 'geojson'

    def fetch(self, region, station, water_body):
        res = req.get(self.api_url + '?q=Polska%' + region + '%' + station + '%' + water_body + '&format=' + self.format)
        print(self.api_url + '?q=Polska%' + region + '%' + station + '%' + water_body + '&format=' + self.format)
        return res.json()

    def format_station(station):
        return station.replace(' ', '+')
    

    def format_water_body(water_body):
        if(water_body.find('Jez.') != -1):
            water_body.replace('Jez.', '')
        if(water_body.find(' ') != -1):
            water_body.replace(' ', '+')
        return water_body
        

    


    
