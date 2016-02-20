#!/usr/bin/python
#
# Adapted from script by Diana MacLean 2011
#
# Mapper script adapted for CS448G from Amazon's example: http://aws.amazon.com/jobflows/2273?_encoding=UTF8&jiveRedirect=1
#
#

import sys
import re

def getStopWords(filePath):
	stoppattern = re.compile("'([a-zA-Z])'")
	stopWords = []
	with open(filePath, 'r') as f:
		for line in f:
			for word in stoppattern.findall(line):
				stopWords.append(word)

	toReturn = set(stopWords)
	return toReturn

def main(argv):

	stopWords = getStopWords("stop-words")
	line = sys.stdin.readline()
	pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
	try:
		while line:
			for word in pattern.findall(line):
				#check for stop words
				if not word in stopWords:
					print(word.lower() + "\t" + "1")
			line =  sys.stdin.readline()
	except "end of file":
		return None
if __name__ == "__main__":
	main(sys.argv)
