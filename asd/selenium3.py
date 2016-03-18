#!/usr/bin/env python
from selenium import webdriver
import datetime
#now = datetime.datetime.now()

#from selenium.webdriver.common.keys import Keys

########            SERWISY               #####
''
LISTA_SERWISOW = ["http://www.finanse.wp.pl",
"http://www.tech.wp.pl",
"http://www.dzieci.pl",
"http://www.pudelek.pl",
"http://www.kobieta.wp.pl",
"http://www.sportowefakty.wp.pl",
"http://www.tv.wp.pl",
"http://www.wp.tv",
"http://www.gry.wp.pl",
"http://www.praca.wp.pl",
"http://www.poczta.wp.pl",
"http://www.money.pl",
"http://www.wiadomosci.wp.pl",
"http://www.pogoda.wp.pl",
"http://www.topnews.wp.pl",
]

LISTA_SERWISOW2 = ["http://www.pudelek.pl"]
''
#############################################

gafjs=0
rekid=0
rekidrpos=0
fsc=0
bargif=0
documentwrite=0
pliki=0

##############################################

driver = webdriver.Firefox()

for i in range (0, len(LISTA_SERWISOW)):
	driver.get(LISTA_SERWISOW[i])
	print "+++++++++++++++++++++++++++++++++++++++++++++++"
	now = datetime.datetime.now()
	print now.isoformat()
	print LISTA_SERWISOW[i]
	#print "+++++++++++++++++++++++++++++++"
	#print driver.current_url
	#print driver.page_source
	adres_serwisu=driver.current_url
	driver.find_elements(By.name
	
############################# dziala, ale pokazuje tylko to co jest w zrodle...
 
	if "gaf.js" in driver.page_source:
		
		print "gaf.js is present"
		gafjs=gafjs+1
	else: 
		print "gaf.js is not present"

##############################

	if "rekid" in driver.page_source:

		if "rpos" in driver.page_source:

			print "rekid is present with rpos"
			rekidrpos=rekidrpos+1
		else:
			print "rekid is present"
			rekid=rekid+1
	else:
		print "rekid is not present"


##############################

	if "fsc" in driver.page_source:

        	print "fsc is present"
		fsc=fsc+1
	else:
        	print "fsc is not present"

##############################

	if "bar.gif" in driver.page_source:

        	print "bar.gif is present"
		bargif=bargif+1
	else:
        	print "bar.gif is not present"

##############################

	if "document.write" in driver.page_source:

		print "document.write is present"
		documentwrite=documentwrite+1
	else:
		print "document.write is not present"

#############################
	if "/pliki/" in driver.page_source:
		
		print "/pliki/ is present"
		pliki=pliki+1
	else:	
		print "/pliki/ is not present"

''
###############################################################
#print adres_serwisu


#assert "tech" in driver.page_source


#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
print "sprawdzilem", len(LISTA_SERWISOW), "serwisow"
print "===liczba wystapien poszczegolnych elementow==="
print "gaf.js=", gafjs 
print "rekid=", rekid
print "rekidrpos=", rekidrpos
print "fsc=", fsc
print "bar.gif=", bargif
print "document.write=", documentwrite
print "/pliki/=", pliki


# gafjs="gafj
driver.close()

#print gafjs="gafjs"

#"rekid="rekid, "rekidrpos="rekidrpos, "fsc="fsc, "bargif="bargif, "documentwrite="documentwrite, "pliki="pliki 


