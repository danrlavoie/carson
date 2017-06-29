
"""
Removes all non-proper-noun capitals from a given text.
Removes capital letters from text, even for Bill Clinton.
Accepts as input a non-tokenized string.
There are multiple types of cap-removal to do.
greedy: removes all caps. GOAL -> goal, Mr. -> mr., Cook -> cook
preserve_nnp: removes capitalization that isn't a proper noun.
"""
import re
from textblob import TextBlob
class TextParse:
	"""
	Removes all nonessential punctuation from a text.
	Returns the text as a single string separated by spaces.
	"""
	def remove_punctuation(self, data):
		results = []
		tokenizer = re.compile(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+')
		data = "".join(tokenizer.split(data))
		results.append(data)
		return data
	def remove_caps_greedy(self, data):
		results = []
		data = data.lower()
		results.append(data)
		return data

	def remove_caps_preserve_nnp(self, data):
		print(data)
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

	def find_ngrams(self, input_list, n):
		'''Returns the set of n consecutive tuples from input_list'''
		return zip(*[input_list[i:] for i in range(n)])

