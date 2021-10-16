from bs4 import BeautifulSoup
import xmltodict
import lxml
import json

with open("scan.xml") as f:
    data_dict = xmltodict.parse(f.read())
f.close()
json_data = json.dumps(data_dict)
json_data = json.loads(json_data)
allscannedports = json_data['nmaprun']["scaninfo"]["@services"]
scannedports_list = allscannedports.split(',')

print(json_data['nmaprun']['host']['address']['@addr'])
