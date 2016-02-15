#!/usr/bin/env python
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
	else
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
		"yesterday" :	datetime.today() + timedelta(days=-1)
		"today" 	:	datetime.today()
		"tonight"	:	datetime.today()
		"tomorrow morning"	:	datetime.today + timedelta(days=1)
		"tomorrow" 			:	datetime.today() + timedelta(days=1)
		"Monday"			:	getNextWeekday(weekdays["monday"])
		"Tuesday"			:	getNextWeekday(weekdays["tuesday"])
		"Wednesday"			:	getNextWeekday(weekdays["wednesday"])
		"Thursday"			:	getNextWeekday(weekdays["thursday"])
		"Friday"			:	getNextWeekday(weekdays["friday"])
		"Saturday"			:	getNextWeekday(weekdays["saturday"])
		"Sunday"			:	getNextWeekday(weekdays["sunday"])
		"this weekend"		:	with getNextWeekday(weekdays["friday"]) as firstDate: getDates(firstDate, firstDate + timedelta(days=3))
		"next week"			:	with getNextWeekday(weekdays["monday"]) as firstDate: getDates(firstDate, firstDate + timedelta(days=7))	
		"next month"
		"next year"
		"this week"			:	
		"this month"
		"this year"
		"last week"			:	
		"last month"
		"last year"
	}
def interpretMessage(word_list):
	print(word_list)
	if (any(s in word_list for s in ["weather","rain","sun","hot","cold","warm","snow","humid","pollen","temperature"])):
		print("I believe you asked me about the weather just now.")
	elif (any(s in word_list for s in ["calendar","agenda"])):
		print("I will try to look at your schedule.")



def greet():
	greeting_list = [
		"Good morning, sir",
		"How are you doing today, sir?",
		"What can I do for you?",
	]
def main():
	greet()
	input_message = ""
	input_words = []
	while ("quit" not in input_words):
		input_message = input()
		print("Your input was: " + input_message)
		cleaned_input = RemovePunct().run(input_message)
		cleaned_input = RemoveCapsPreserveNNP().run(cleaned_input)
		input_words = cleaned_input.split(" ")
		print("I cleaned the input, now it looks like: " + cleaned_input)
		interpretMessage(input_words)
if __name__ == '__main__':
	main()
