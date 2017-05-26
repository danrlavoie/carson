import json
import requests
from src.logger import Logger

class Location:
	def __init__(self):
		pass
	def getLocation(self, feature='weather'):
		if(not Logger().checkForResponse('location')):
			filename = 'var/' + 'location' + '.json'
			with open(filename, 'r') as fp:
				response = json.load(fp)	
		else:
			url= 'http://ip-api.com/json'
			r = requests.get(url)
			response = json.loads(r.text)
		self.parseLocationResponse(response)
		Logger().storeResponse('location',response)
		if feature == 'weather':
			return response['region'] + '/' + response['city']
	def parseLocationResponse(self, response):
		response['country']
		response['region']
		response['regionName']
		response['city']
		response['zip']
		response['lat']
		response['lon']
		print(response['city'] + ", " + response['region'])