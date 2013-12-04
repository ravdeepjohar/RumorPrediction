# from HTMLParser import HTMLParser
# from htmlentitydefs import name2codepoint

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print "Start tag:", tag
#         for attr in attrs:
#             print "     attr:", attr
#     def handle_endtag(self, tag):
#         print "End tag  :", tag
#     def handle_data(self, data):
#         print "Data     :", data
#     def handle_comment(self, data):
#         print "Comment  :", data
#     def handle_entityref(self, name):
#         c = unichr(name2codepoint[name])
#         print "Named ent:", c
#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = unichr(int(name[1:], 16))
#         else:
#             c = unichr(int(name))
#         print "Num ent  :", c
#     def handle_decl(self, data):
#         print "Decl     :", data

# parser = MyHTMLParser()

# files = open('9-11stamp.htm',"r")
# s=files.read()

# #parser.feed(s)

# from lxml import etree
# #data = open('result.html','r').read()
# parser = etree.HTMLParser()
# doc = etree.HTML(s)
# #tree  = etree.parse(s, parser)

# result = etree.tostring(doc, pretty_print=True, method="html")
# #print result   

# # result = etree.tostring(tree.getroot(),
# #                     pretty_print=True, method="html")
# # print(result)

# for tr in doc.xpath('//tr//td//p//b'):
#    print tr.xpath('./text()')


from bs4 import BeautifulSoup
#9-11stamp.htm or 1895exam.htm
soup = BeautifulSoup(open("hager.htm"))
#print soup.title
strin = soup.get_text


strin = soup.find_all('b')

for s in strin:

	sysdf = s.getText().strip('\t\n ').encode('utf8')
	import re
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

	   
	    print a[len(a)-1]
	  

	# if s.getText() == "The Truth":
	# 	b =  s.parent

	# 	for yo in b.find_all('font')
	# 		print yo.getText().encode('utf8')



# for s in strin:
#     print(s.getText().encode('utf8'))