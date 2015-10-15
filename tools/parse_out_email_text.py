#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        and return a string that contains all the words
        in the email (space-separated)
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        """
    f.seek(0)
    all_text = f.read()

    ### split metadata off
    content = all_text.split("X-FileName:")
    words = ""
    st = ""
    if len(content) > 1:
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        stemmer = SnowballStemmer("english")
#	print tree
    for word in text_string.split():
        st = st+" "+(stemmer.stem(word))

    words = st.lstrip()
    return words

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()
