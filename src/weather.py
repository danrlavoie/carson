import json
import requests
from src.logger import Logger

class Weather:
	def __init__(self):
		pass
	def getWeather(self, feature, firstdate=1225, seconddate=1231, location="MA/Boston"):
		api = "9e203c14c8a68a24/"
		url_front = 'http://api.wunderground.com/api/'
		url_penult = '/q/'
		url_format = '.json'
		url_location = location
		#Hourly
		#Planner_MMDDMMDD
		#Yesterday
		#TODO: Add extra weather lookups
		#TODO: Save request to disk and only request again if it has been more than 30 minutes since last check
		if(not Logger().checkForResponse(feature)):
			filename = 'var/' + feature + '.json'
			with open(filename, 'r') as fp:
				response = json.load(fp)	
		else:
			url = url_front + api + feature + url_penult + url_location + url_format
			r = requests.get(url)
			response = json.loads(r.text)
		if feature == 'forecast':
			self.parseWeatherForecastResponse(response)
		elif feature == 'forecast10day':
			self.parseWeatherForecastResponse(response)
		elif feature == 'conditions':
			self.parseWeatherConditionsResponse(response)
		elif feature == 'almanac':
			self.parseWeatherAlmanacResponse(response)
		elif feature == 'hourly':
			self.parseWeatherHourlyResponse(response)
		elif feature == 'hourly10day':
			self.parseWeatherHourlyResponse(response)
		elif feature == 'planner':
			self.parseWeatherPlannerResponse(response)
		elif feature == 'yesterday':
			self.parseWeatherYesterdayResponse(response)
		Logger().storeResponse(feature, response)
	def parseWeatherConditionsResponse(self, response):
		location = response['current_observation']['display_location']['full']
		temp_f = response['current_observation']['temp_f']
		feelslike_f = response['current_observation']['feelslike_f']
		weather = response['current_observation']['weather']
		wind_string = response['current_observation']['wind_string']
		print('Right now in ' + location + ' it is ' + str(temp_f) + ' degrees out and it feels like ' + str(feelslike_f) + '.')
		print("It's " + weather.lower() + " and the wind is blowing " + wind_string[0].lower() + wind_string[1:] + '.')

	def parseWeatherForecastResponse(self, response):
		print("\n".join(
			[
				(elem['title'] + ': ' + elem['fcttext']) 
				for elem in response['forecast']['txt_forecast']['forecastday']
			]
		))
	def parseWeatherAlmanacResponse(self, response):
		print("For today's date, the normal high temperature is " + response['almanac']['temp_high']['normal']['F'] +
				" degrees and the record was " + response['almanac']['temp_high']['record']['F'] +
				", set in " + response['almanac']['temp_high']['recordyear'] +
				".")
		print("The normal low temperature is " + response['almanac']['temp_low']['normal']['F'] +
				" and the record was " + response['almanac']['temp_low']['record']['F'] +
				", set in " + response['almanac']['temp_low']['recordyear'] +
				".")
	def parseWeatherPlannerResponse(self, response):
		pass
	def parseWeatherYesterdayResponse(self, response):
		pass
	def parseWeatherHourlyResponse(self, response):
		print("\n".join(
			[
				(elem['FCTTIME']['pretty'] + ': '  + 
					elem['condition'] + ', ' + 
					elem['temp']['english'] +  ' degrees. \n\t Wind from the ' +  
					elem['wdir']['dir'] + ' at ' + 
					elem['wspd']['english'] + ' miles per hour. Chance of precipition ' +
					elem['pop'] + ' percent.')
				for elem in response['hourly_forecast']
			]
		))