from bs4 import BeautifulSoup
import xmltodict
import lxml
import json

with open("scan.xml") as f:
    data_dict = xmltodict.parse(f.read())
f.close()
json_data = json.dumps(data_dict)
json_data = json.loads(json_data)
ports = json_data['nmaprun']['host']['ports']['port']
for i in ports:
    print(i['@portid'])
    for g in i['service']:
        print(i['service'][g])
    print('\n\n')


