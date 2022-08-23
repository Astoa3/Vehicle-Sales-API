#!/usr/bin/python

import requests
import anvil.server
anvil.server.connect("7WMQKMUFHJAHI4ZTKZ5H4VXY-NMYS5F4YHJIRNU3S")
import mysql.connector


#Retreive URL
@anvil.server.callable
def getUrl():
 url = 'https://virtserver.swaggerhub.com/AASTORGA_1/VehicleStore/1/inventory/'
 return url

#Format Requests
@anvil.server.callable
def getRequest(url):
 rsp = requests.get(url)
 rspJSON = rsp.json()
 return rspJSON


anvil.server.wait_forever()
