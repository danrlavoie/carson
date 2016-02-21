#!/usr/bin/env python
import requests

"""
Removes all nonessential punctuation from a text.
Returns the text as a single string separated by spaces.
"""
from nltk.tokenize import RegexpTokenizer
class RemovePunct:
    def run(self, data):
        results = []
        tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
        data = " ".join(tokenizer.tokenize(data))
        results.append(data)
        return data
"""
Removes all non-proper-noun capitals from a given text.
Removes capital letters from text, even for Bill Clinton.
Accepts as input a non-tokenized string.
There are multiple types of cap-removal to do.
greedy: removes all caps. GOAL -> goal, Mr. -> mr., Cook -> cook
preserve_nnp: removes capitalization that isn't a proper noun.
"""
from textblob import TextBlob
class RemoveCapsGreedy:
    def run(self, data):
        results = []
        data = data.lower()
        results.append(data)
        return data

class RemoveCapsPreserveNNP:
    def run(self, data):
        results = []
        blob = TextBlob(data)
        tags = blob.tags
        words = list()
        wordCount = 0
        tokenCount = 0
        while(tokenCount < len(blob.tokens)):
            if blob.tokens[tokenCount][0].isalpha():
                if tags[wordCount][1] != 'NNP':
                    words.append(blob.words[wordCount].lower())
                else:
                    words.append(blob.words[wordCount])
                wordCount += 1
            else:
                words[len(words)-1] = ''.join(
                [words[len(words)-1],blob.tokens[tokenCount]])
            tokenCount += 1
        data = (' '.join(words))
        results.append(data)
        return data
def getNextWeekday(weekday):
	'''Expects weekday to be an integer from 0-6 where 0 represents Monday and 6 Sunday
	'''
	todayDay = datetime.today()
	todayWeekday = todayDay.weekday()
	diff = weekday - todayWeekday
	if diff == 0:
		return todayDay + datetime.timedelta(days=7)
	else:
		return  todayDay + datetime.timedelta(days=diff)

def getDates(startDate, endDate):
	'''Returns a list of dates from the start date (inclusive) to the end date (noninclusive)
	'''
	delta = endDate - startDate
	return([startDate + timedelta(days=i) for i in range(delta.days)])

def parseTimeWords(time_words):
	weekdays = {
		"monday"	:	0,
		"tuesday"	:	1,
		"wednesday"	:	2,
		"thursday"	:	3,
		"friday"	:	4,
		"saturday"	:	5,
		"sunday"	:	6,
	}
	{
		"yesterday" :	datetime.today() + timedelta(days=-1),
		"today" 	:	datetime.today(),
		"tonight"	:	datetime.today(),
		"tomorrow morning"	:	datetime.today + timedelta(days=1),
		"tomorrow" 			:	datetime.today() + timedelta(days=1),
		"Monday"			:	getNextWeekday(weekdays["monday"]),
		"Tuesday"			:	getNextWeekday(weekdays["tuesday"]),
		"Wednesday"			:	getNextWeekday(weekdays["wednesday"]),
		"Thursday"			:	getNextWeekday(weekdays["thursday"]),
		"Friday"			:	getNextWeekday(weekdays["friday"]),
		"Saturday"			:	getNextWeekday(weekdays["saturday"]),
		"Sunday"			:	getNextWeekday(weekdays["sunday"]),
		"this weekend"		:	getDates(getNextWeekday(weekdays["friday"]),getNextWeekday(weekdays["friday"]) + timedelta(days=3)),
		"next week"			:	getDates(getNextWeekday(weekdays["monday"]),getNextWeekday(weekdays["monday"]) + timedelta(days=7)),	
		"next month"		: -1,
		"next year"			: -1,
		"this week"			: -1,
		"this month"		: -1,
		"this year"			: -1,
		"last week"			: -1,
		"last month"		: -1,
		"last year"			: -1,
	}
def find_ngrams(input_list, n):
	'''Returns the set of n consecutive tuples from input_list'''
	return zip(*[input_list[i:] for i in range(n)])

import json
def getWeather(feature, firstdate=1225, seconddate=1231, location="MA/Boston"):
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
	if(not checkForResponse(feature)):
		filename = 'var\\' + feature + '.json'
		with open(filename, 'r') as fp:
			response = json.load(fp)	
	else:
		url = url_front + api + feature + url_penult + url_location + url_format
		r = requests.get(url)
		response = json.loads(r.text)
	if feature == 'forecast':
		parseWeatherForecastResponse(response)
	elif feature == 'forecast10day':
		parseWeatherForecastResponse(response)
	elif feature == 'conditions':
		parseWeatherConditionsResponse(response)
	elif feature == 'almanac':
		parseWeatherAlmanacResponse(response)
	elif feature == 'hourly':
		parseWeatherHourlyResponse(response)
	elif feature == 'hourly10day':
		parseWeatherHourlyResponse(response)
	elif feature == 'planner':
		parseWeatherPlannerResponse(response)
	elif feature == 'yesterday':
		parseWeatherYesterdayResponse(response)
	storeResponse(feature, response)
def parseWeatherConditionsResponse(response):
	location = response['current_observation']['display_location']['full']
	temp_f = response['current_observation']['temp_f']
	feelslike_f = response['current_observation']['feelslike_f']
	weather = response['current_observation']['weather']
	wind_string = response['current_observation']['wind_string']
	print('Right now in ' + location + ' it is ' + str(temp_f) + ' degrees out and it feels like ' + str(feelslike_f) + '.')
	print("It's " + weather.lower() + " and the wind is blowing " + wind_string[0].lower() + wind_string[1:] + '.')

def parseWeatherForecastResponse(response):
	print("\n".join(
		[
			(elem['title'] + ': ' + elem['fcttext']) 
			for elem in response['forecast']['txt_forecast']['forecastday']
		]
	))
def parseWeatherAlmanacResponse(response):
	print("For today's date, the normal high temperature is " + response['almanac']['temp_high']['normal']['F'] +
			" degrees and the record was " + response['almanac']['temp_high']['record']['F'] +
			", set in " + response['almanac']['temp_high']['recordyear'] +
			".")
	print("The normal low temperature is " + response['almanac']['temp_low']['normal']['F'] +
			" and the record was " + response['almanac']['temp_low']['record']['F'] +
			", set in " + response['almanac']['temp_low']['recordyear'] +
			".")
def parseWeatherPlannerResponse(response):
	pass
def parseWeatherYesterdayResponse(response):
	pass
def parseWeatherHourlyResponse(response):
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
import os.path
import datetime as dt
from datetime import datetime
def checkForResponse(request):
	'''Returns true if it has been more than 30 minutes since the request was run'''
	filename = 'var\\' + request + '.json'
	if (os.path.isfile(filename)):
		t = os.path.getmtime(filename)
		mod_time = datetime.fromtimestamp(t)
		if (not(datetime.now() - mod_time > dt.timedelta(minutes=15))):
			return False
	return True
def storeResponse(request, response):
	filename = 'var\\' + request + '.json'
	with open(filename, 'w') as fp:
	    json.dump(response, fp)
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
def interpretMessage(word_list):
	time_words = [
		"morning"
		"afternoon"
		"evening"
		"night"
		"this"
		"next"
		"last"
		"yesterday",
		"today",	
		"tonight",
		["tomorrow","morning"],
		"tomorrow",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
		"Sunday",
		["this","weekend"],
		["next","week"],
		"next month",
		"next year",
		"this week",
		"this month",
		"this year",
		"last week",
		"last month",
		"last year",
	]
	print(word_list)
	if (any (s in word_list for s in time_words)):
		for s in word_list:
			if s in time_words:
				print(s)
		print("I think you were asking about something relating to a specific time.")
	if (any(s in word_list for s in ["weather","rain","sun","hot","cold","warm","snow","humid","pollen","temperature"])):
		getWeather('forecast', location=getLocation())
	elif (any(s in word_list for s in ["calendar","agenda"])):
		print("I will try to look at your schedule.")
import random
def greet():
	greeting_list = [
		"Good morning, sir",
		"How are you doing today, sir?",
		"What can I do for you?",
	]
	print(random.choice(greeting_list))
def main():
	greet()
	input_message = ""
	input_words = []
	while ("quit" not in input_words):
		input_message = input('-')
		print("Your input was: " + input_message)
		cleaned_input = RemovePunct().run(input_message)
		cleaned_input = RemoveCapsPreserveNNP().run(cleaned_input)
		input_words = cleaned_input.split(" ")
		print("I cleaned the input, now it looks like: " + cleaned_input)
		interpretMessage(input_words)
if __name__ == '__main__':
	main()
