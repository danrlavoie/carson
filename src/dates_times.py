#!/usr/bin/env python

class DatesTimes:
	def __init__(self):
		self.time_words = [
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
	def getNextWeekday(self, weekday):
		'''Expects weekday to be an integer from 0-6 where 0 represents Monday and 6 Sunday
		'''
		todayDay = datetime.today()
		todayWeekday = todayDay.weekday()
		diff = weekday - todayWeekday
		if diff == 0:
			return todayDay + datetime.timedelta(days=7)
		else:
			return  todayDay + datetime.timedelta(days=diff)

	def getDates(self, startDate, endDate):
		'''Returns a list of dates from the start date (inclusive) to the end date (noninclusive)
		'''
		delta = endDate - startDate
		return([startDate + timedelta(days=i) for i in range(delta.days)])

	def parseTimeWords(self, time_words):
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
