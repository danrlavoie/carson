#!/usr/bin/env python

from src.text_parse import RemovePunct, RemoveCapsPreserveNNP
from src.dates_times import DatesTimes
from src.weather import Weather
from src.location import Location

def interpretMessage(word_list):
	print(word_list)
	if (any (s in word_list for s in DatesTimes().time_words)):
		for s in word_list:
			if s in DatesTimes().time_words:
				print(s)
		print("I think you were asking about something relating to a specific time.")
	if (any(s in word_list for s in ["weather","rain","sun","hot","cold","warm","snow","humid","pollen","temperature"])):
		Weather().getWeather('hourly', location=Location().getLocation())
	elif (any(s in word_list for s in ["calendar","agenda"])):
		print("I will try to look at your schedule.")

def main():
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
