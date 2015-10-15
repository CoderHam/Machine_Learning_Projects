#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.
    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris).
    The actual documents are in the Enron email dataset.
    The data is stored in lists and packed away in pickle files at the end
"""

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []
sw = ["sara", "shackleton", "chris", "germani"]

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        #if temp_counter < 200:
        path = os.path.join('..', path[:-1])
        print "In: ", path
        email = open(path, "r")

        words_stem = str(parseOutText(email))
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
        for word in sw:
            if(word in words_stem):
                words_stem = words_stem.replace(word, "")
        word_data.append(words_stem)### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if name is "sara":
            from_data.append("0")
        elif name is "chris":
            from_data.append("1")
        email.close()

print "All emails processed"
from_sara.close()
from_chris.close()
#print "\nWord Data element 152: ", word_data[152]
pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
vector = TfidfVectorizer(stop_words = "english")
bag = vector.fit_transform(word_data)
words_list = vector.get_feature_names()
print "No. of words: ",len(words_list)
print "For Eg, Word no. 34597: ",words_list[34597]
# bag = vector.transform(email_list)
# print bag
# print vector.vocabulary_.get("word")
# import nltk
# nltk.download()
# from nltk.corpus import stopwords
# swords = stopwords.words("english")
# len(sw)
# from nltk.stem.snowball import SnowballStemmer
# stemmer = SnowballStemmer("english")
# stemmer.stem("word")
