import json
import xmltodict
f = open("YottaAnts3.xml")
xml_content = f.read()
f.close()
print(json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True))
