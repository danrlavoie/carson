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

def find_ngrams(input_list, n):
    '''Returns the set of n consecutive tuples from input_list'''
    return zip(*[input_list[i:] for i in range(n)])

