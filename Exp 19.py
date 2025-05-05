#Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.

import string

def remove(sen):
	trans = str.maketrans('','',string.punctuation)
	return sen.translate(trans)

str = input()
modified = remove(str)
print(modified)