from bs4 import BeautifulSoup
import os, re, csv
testcount = 0
count = 0
def main():
	global count
	
	protitlecsv = open('protitlecsv.csv', 'rb')
	summarytitlecsv = open('summarytitlecsv.csv', 'wb')

	os.chdir("dataset")

	for line in protitlecsv:

		filelocation = line.split(",")[0]
		
		if filelocation.endswith('.htm'):
				soup = BeautifulSoup(open(filelocation))
				#count += 1
				storeSummary(soup,summarytitlecsv,filelocation)

	protitlecsv.close()
	summarytitlecsv.close()

	print testcount

		
	

def storeSummary(soup, writecsv,filelocation):

	#9-11stamp.htm or 1895exam.htm
	global testcount
	
	summary = ""
	
	#print soup.title.get_text().encode('utf8')
	strin = soup.get_text
	

	strin = soup.find_all('b')

	for s in strin:


		sysdf = s.getText().strip('\t\n ').encode('utf8')
		
		pat = re.compile(r'\s+')
		# = '  \t  foo   \t   bar \t  '
		pr =  pat.sub('', sysdf)
		#print pr

		if "summaryoferumor" in pr.lower() or "summaryoftheerumor" in pr.lower() or "summaryofrumor" in pr.lower() or "TheeRumor" in pr or "summaryoforiginalerumor" in pr.lower() or "summaryerumor" in pr.lower():
		#if "summaryoferumor" in pr.lower() or "summaryoftheerumor" in pr.lower() or "summaryofrumor" in pr.lower() or "TheeRumor" in pr or "summaryoforiginalerumor" in pr.lower():
			b =  s.parent
			b = b.parent
			#print b

			summary = getsummary(b)
			
			# a = []
			# for yo in b.find_all('font'):
			# 	#print yo.getText().encode('utf8')
			# 	a.append(yo.getText().encode('utf8'))

			# #print a 

			# if len(a) != 0:
			# 	temp = (a[len(a)-1]).replace("\n", "").replace(",", "").replace("\t", "").replace("\r", "")
			# 	summary = re.sub(' +',' ',temp) 
			# 	testcount += 1
			# else:
			# 	print filelocation


			   
		
	writecsv.write(filelocation + "," + summary + "\n")
		
	
def getsummary(b):
	summary = ""
	a = []
	for yo in b.find_all('font'):
		#print yo.getText().encode('utf8')
		a.append(yo.getText().encode('utf8'))

	#print a 

	# if len(a) != 0:
	# 	# temp = (a[len(a)-1]).replace("\n", "").replace(",", "").replace("\t", "").replace("\r", "")
	# 	# summary = re.sub(' +',' ',temp) 
	# 	summary = a[0]

	if len(a) != 0:

		if "summary" in a[0].lower() or a[0] == " ":
				pass
		else:
			temp = (a[0]).replace("\n", "").replace(",", "").replace("\t", "").replace("\r", "")
			summary += re.sub(' +',' ',temp) + " "

		# for i in range(1,len(a)):
		# 	if a[i] == " " or "Summary of the eRumor" in a[i] or "Summary of eRumor" in a[i]:
		# 		pass
		# 	else:
		# 		temp = (a[i]).replace("\n", "").replace(",", "").replace("\t", "").replace("\r", "")
		# 		summary += re.sub(' +',' ',temp) + " "

		for i in range(1,len(a)):

			temp = (a[i]).replace("\n", "").replace(",", "").replace("\t", "").replace("\r", "")
			temp = re.sub(' +',' ',temp)			

			if temp == " " or "Summary of the eRumor" in temp or "Summary of eRumor" in temp:
				pass
			else:				
				summary += temp + " "

		
	else:
		summary = getsummary(b.parent)

	return summary



# 	if s.getText() == "The Truth":
# 		b =  s.parent

# 		for yo in b.find_all('font')
# 			print yo.getText().encode('utf8')



# for s in strin:
#     print(s.getText().encode('utf8'))



if __name__ == '__main__':
	main()