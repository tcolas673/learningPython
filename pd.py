import pandas as pd;
import xmltodict
import xml.etree.ElementTree as ET
import json
import os


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'results.xml')

tree = ET.parse(my_file)
xml_data = tree.getroot()
xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

columns = ['company_name', 'login', 'approved_scope', 'address', 'city', 'state', 'country', 'zip_code', 'contact_information']
dataframe = pd.DataFrame(columns = columns)

namespaces = { 
    'Result': None,
    'Row': None,
}
data = xmltodict.parse(xmlstr)

# print(xmlstr)