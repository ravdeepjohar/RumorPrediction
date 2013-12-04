from bs4 import BeautifulSoup
import os, re, csv

count = 0
def main():
	global count
	titlecsv = open('titlecsv.csv', 'wb')
	os.chdir("dataset")

	

	for letter in os.listdir("."):

		for files in os.listdir(letter):
			readfile = letter+"/"+files
			if readfile.endswith('.htm'):
				soup = BeautifulSoup(open(readfile))
				#storeTitle(readfile,soup)
				storeSummary(soup)
				#count += 1


	titlecsv.close()
	#print count

def storeTitle(soup,csvfile):


	tit =  soup.title.get_text().encode('utf8')

	csvfile.write(tit+"\n")




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