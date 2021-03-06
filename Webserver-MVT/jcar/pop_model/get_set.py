from jcar.utils.utils import Util
import ast
from datetime import datetime

class GetSet():

    def __init__(self):
        self.data = {'gas': None,
                     'bat': None,
                     'lat': None,
                     'lon': None,
                     'sal': None,
                     'dad': None,
                     'tsp': None,
                     'gsm': None,
                     'maps': None
                     }

        self.history = {'gas': None,
                     'bat': None,
                     'lat': None,
                     'lon': None,
                     'sal': None,
                     'dad': None,
                     'tsp': None,
                     'gsm': None,
                     'maps': None
                     }

    def read_history(self):
        load = open('database/history.json')
        self.history = ast.literal_eval( load.read() )

    def write_history(self):
        self.read_history()
        utc_hm = self.data['tsp'][-6:-2]
        self.history[utc_hm] = self.data

        json = open ('database/history.json', 'w')
        json.write( str(self.history) )
        json.close()

    def read_json(self):
        load = open('database/informations.json')
        self.data = ast.literal_eval( load.read() )

    def write_json(self):
        req_min = int(self.data['tsp'][-4:-2])

        if req_min % 1 == 0:
            self.write_history()

        json = open ('database/informations.json', 'w')
        json.write( str(self.data) )
        json.close()

    def get_history(self):
        self.read_history()
        return self.history

    def set_data(self, gas, bat, lat, lon, tsp, gsm):
        self.read_json()

        self.data ['gas'] = gas
        self.data ['bat'] = bat
        self.data ['lat'] = lat
        self.data ['lon'] = lon
        self.data ['tsp'] = tsp
        self.data ['gsm'] = gsm
        self.data ['maps'] = "http://maps.google.com/maps?q="+lat+","+lon

        self.write_json()

        return self.data

    def get_data(self):
        self.read_json()
        return self.data

    def set_balance(self, sal, dad):
        self.read_json()

        self.data ['sal'] = sal
        self.data ['dad'] = dad

        self.write_json()

        return self.data

    def get_id(self, id):
        self.get_history()
        return self.history[str(id)]
