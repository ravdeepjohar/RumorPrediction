from bs4 import BeautifulSoup
import os, re, csv

def main():


	summarytitlecsv = open('summarytitlecsv.csv', 'rb')
	completecsv = open('completecsv.csv', 'wb')

	os.chdir("dataset")
	for line in summarytitlecsv:

		splits = line.split(",")

		filelocation = splits[0]
		soup = BeautifulSoup(open(filelocation))
		title, label = storeTitle(soup)
		summary = splits[1].replace("\n", "")

		if summary != "":

			completecsv.write(filelocation + "," + title + "," + summary + "," + str(label) + "\n")
		#print filelocation + "," + title + "," + summary + "," + str(label) + "\n"
		#completecsv.write(summary)

	summarytitlecsv.close()
	completecsv.close()




def storeTitle(soup):


	tit =  soup.title.get_text().encode('utf8').replace("\n", "").replace(",", "").rsplit("-", 1)
	label = 0
	
	if "truth" in tit[1].lower():
		label = 1

	# for i in range(len(tit)):
	# 	st = st + "," + tit[i]

	return tit[0] , label



if __name__ == '__main__':
	main()