import json
import requests

def getLocation(feature='weather'):
	if(not checkForResponse('location')):
		filename = 'var\\' + 'location' + '.json'
		with open(filename, 'r') as fp:
			response = json.load(fp)	
	else:
		url= 'http://ip-api.com/json'
		r = requests.get(url)
		response = json.loads(r.text)
	parseLocationResponse(response)
	storeResponse('location',response)
	if feature == 'weather':
		return response['region'] + '/' + response['city']
def parseLocationResponse(response):
	response['country']
	response['region']
	response['regionName']
	response['city']
	response['zip']
	response['lat']
	response['lon']
	print(response['city'] + ", " + response['region'])