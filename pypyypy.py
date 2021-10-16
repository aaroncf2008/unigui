from bs4 import BeautifulSoup
import xmltodict
import lxml
import json

with open('scan.xml') as f:
    data_dict = xmltodict.parse(f.read())

f.close()

json_data = json.dumps(data_dict)

json_data = json.loads(json_data)

ports = json_data['nmaprun']['host']['ports']['port']
text4=''
gg = json_data['nmaprun']['host']['ports']['port'][0]['service']
for i in gg:
            text4 = text4 + f'{gg[i]}\n'
print(text4)