from bs4 import BeautifulSoup
import os, re, csv

count = 0
def main():
	global count
	titlecsv = open('titlecsv.csv', 'wb')
	readtitlecsv = open('titlecsv.csv', 'rb')
	protitlecsv = open('protitlecsv.csv', 'wb')
	os.chdir("dataset")

	

	for letter in os.listdir("."):

		for files in os.listdir(letter):
			readfile = letter+"/"+files
			if readfile.endswith('.htm'):
				soup = BeautifulSoup(open(readfile))
				storeTitle(soup,titlecsv,readfile)
				#storeSummary(soup)
				#count += 1

	count(readtitlecsv,protitlecsv)
	readtitlecsv.close()
	protitlecsv.close()
	#print count

def storeTitle(soup,csvfile,readfile):


	tit =  soup.title.get_text().encode('utf8').replace("\n", "").replace(",", "").rsplit("-", 1)

	st = readfile

	for i in range(len(tit)):
		st = st + "," + tit[i]

	csvfile.write(st+"\n")

def count(csvfile, writefile):

	count = 0 

	for line in csvfile:

		temp = line.split(",")
		

		if(len(temp) > 2):

			if "Truth!" in temp[2] or  "Fiction!" in temp[2]:
				writefile.write(line)
				count += 1

	print count

	





def storeSummary(soup):

	#9-11stamp.htm or 1895exam.htm
	
	#print soup.title.get_text().encode('utf8')
	strin = soup.get_text


	strin = soup.find_all('b')

	for s in strin:


		sysdf = s.getText().strip('\t\n ').encode('utf8')
		
		pat = re.compile(r'\s+')
		# = '  \t  foo   \t   bar \t  '
		pr =  pat.sub('', sysdf)
		#print pr

		if pr == "SummaryofeRumor" or pr == "SummaryoftheeRumor":
			b =  s.parent
			a = []
			for yo in b.find_all('font'):
				#print yo.getText().encode('utf8')
				a.append(yo.getText().encode('utf8'))

			if len(a) != 0:		   
				print a[len(a)-1]

			else:

				print
	  

# 	if s.getText() == "The Truth":
# 		b =  s.parent

# 		for yo in b.find_all('font')
# 			print yo.getText().encode('utf8')



# for s in strin:
#     print(s.getText().encode('utf8'))



if __name__ == '__main__':
	main()