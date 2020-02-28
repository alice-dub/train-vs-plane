import re
import requests

url = 'https://data.opendatasoft.com/api/records/1.0/search/?dataset=osm-world-airports%40babel&q='

aero_codes = {} 

with open('code_ref_EN.csv') as cities:
    for row in cities:
        name = row.split(',')[1]
        for element in name.replace('-', '/').split('/'):
            r = requests.get('{}{}'.format(url, element))
            res = r.json()
            if res.get('records'):
                aero_codes[name[:-1]] = []
                for record in res['records']:
                    if record['fields'].get('iata'):
                        aero_codes[name[:-1]].append(record['fields']['iata'].encode('utf-8'))

with open('code_aero_EN2.csv', 'w') as f:
    [f.write('{0};{1}\n'.format(key, value)) for key, value in aero_codes.items()]