import pandas as pd
from contactType import contactList
from matplotlib import pyplot as plt 
import xml.etree.ElementTree as etree
import os



THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'results.xml')

tree = etree.parse(my_file)
root = tree.getroot()
columns = ['company_name', 'login', 'approved_scope', 'address', 'city', 'state', 'country', 'zip_code', 'contact_name', 'phone_number', 'email']
 

dataframe = pd.DataFrame(columns = columns)

for node in root.findall('Row'):
    
    company_name = node.find("tcb_name").text

    login = node.find("tcb_login").text

    approved_scope = node.find("approved_scope").text

    address = node.find("address").text

    city = node.find("city").text

    state = node.find("state").text

    country = node.find("country").text

    contact_information = node.find("contact_information").text
    contact_name, email, phone_number = contactList(contact_information)
    dataframe = dataframe.append(pd.Series([company_name, login, approved_scope, address, city, state, country, contact_name, email, phone_number]), ignore_index = True)
    print(dataframe.head(2))