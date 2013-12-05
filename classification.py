from random import randrange
import nltk

summary = []
files = []
title = []
torf = []

wordsfreq = {}
testSummary = []
testFiles = []
testTitle = []
testTorf = []

def filldataset():

	dataset = open('dataset.csv', 'rb')



	for line in dataset:
		line = line.split(",")
		files.append(line[0])
		title.append(line[1])
		summary.append(line[2]) 
		torf.append(int(line[3]))


	dataset.close()

	for i in range(int((len(summary)*20.00)/100.00)):
		random_index = randrange(0,len(summary))

		testSummary.append(summary[random_index])
		testFiles.append(files[random_index])
		testTitle.append(title[random_index])
		testTorf.append(torf[random_index])
		

		del summary[random_index]
		del torf[random_index]
		del files[random_index]
		del title[random_index]


def main():

	filldataset()
	extract_features()
	
	# tcount = 0
	# fcount = 0

	# for label in testTorf:

	# 	if label == 0:
	# 		fcount  += 1

	# 	else:

	# 		tcount += 1

	# print tcount, fcount


def extract_features():

	for i in range(len(summary)):

		text = nltk.word_tokenize(summary[i])
		print nltk.pos_tag(text)
		
	
	

def filldict(sent):

	for s in sent:

		for word in s.lower().split(" "):

			if word not in wordsfreq:
				wordsfreq[word] = 1

			else:
				wordsfreq[word] += 1


if __name__ == '__main__':
	main()