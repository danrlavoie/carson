#!/usr/bin/env python
import requests


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
		getWeather('hourly', location=getLocation())
	elif (any(s in word_list for s in ["calendar","agenda"])):
		print("I will try to look at your schedule.")
import random
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
