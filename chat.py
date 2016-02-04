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

def interpretMessage(word_list):
	print(word_list)
	if (any(s in word_list for s in ["weather","rain","sun","temperature"])):
		print("I believe you asked me about the weather just now.")
	elif (any(s in word_list for s in ["calendar","agenda"])):
		print("I will try to look at your schedule.")
def main():
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
