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
	words = "'i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now'"
	stoppattern = re.compile("'([a-zA-Z]*)'")
	stopWords = []
	for word in stoppattern.findall(words):
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
