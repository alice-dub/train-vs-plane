
# The main goal of the script is to extract navitia IDs of SNCF foreign stop points 
#(french stop points ids are INSEE code but foreign stop points IDs ase selated to osm IDs)
import requests
from param import token

url = 'https://api.sncf.com/v1/coverage/sncf/stop_points?start_page='

num_page = 	0
browsed_elements = 0
foreign_cities = {}


r = requests.get('{}{}'.format(url, num_page), headers={'Authorization': token})

res = r.json()
total_element = res['pagination']['total_result']
item_page = res['pagination']['items_on_page']


while browsed_elements < total_element:
    r = requests.get('{}{}'.format(url, num_page), headers={'Authorization': token})
    res = r.json()
    item_page = res['pagination']['items_on_page']
    browsed_elements = browsed_elements + item_page
    for stop_point in res['stop_points']:
        if stop_point.get('administrative_regions'):
            if not stop_point['administrative_regions'][0].get('id').startswith('admin:fr'):
                foreign_cities[stop_point['administrative_regions'][0]['id']] = stop_point['name']
    num_page += 1


with open('code_ref_EN.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key.encode('utf-8'), value.encode('utf-8'))) for key, value in foreign_cities.items()]

