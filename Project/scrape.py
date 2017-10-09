from selenium import webdriver
import urllib2
import bs4 as bs
from bs4.dammit import EntitySubstitution

'''
"https://turo.com/search?location=HOU%20%E2%80%94%20William%20P.%20Hobby%20Airport-Houston%2C%20Houston%2C%20TX&country=&region=&locationType=airport&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&airportCode=HOU",
"https://turo.com/search?location=IAH%20%E2%80%94%20George%20Bush%20Intercontinental%20Airport%2C%20Houston%2C%20TX&locationType=airport&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=&country=&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&airportCode=IAH",
"https://turo.com/search?location=Spring%20Park%20Center%2C%20Houston%2C%20TX%2077373%2C%20USA&locationType=ZIP&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=TX&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=30.0507722&longitude=-95.4286496&defaultZoomLevel=14",
"https://turo.com/search?location=Richmond%20-%20Rosenberg%20Rd%2C%20Houston%2C%20TX%2077063%2C%20USA&locationType=Address&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=TX&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=29.7472258&longitude=-95.53305240000002&defaultZoomLevel=14",
"https://turo.com/search?location=Missouri%20St%2C%20Houston%2C%20TX%2C%20USA&locationType=Address&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=TX&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=29.7441743&longitude=-95.3977811&defaultZoomLevel=14",
'''

AllLinks = [
"https://turo.com/search?location=Arlington%20Heights%2C%20IL%2C%20USA&locationType=City&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=IL&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=42.0883603&longitude=-87.98062650000001&defaultZoomLevel=11",
"https://turo.com/search?location=Naperville%2C%20IL%2C%20USA&locationType=City&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=IL&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=41.7508391&longitude=-88.1535352&defaultZoomLevel=11",
"https://turo.com/search?location=Lincolnwood%2C%20IL%2C%20USA&locationType=City&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=IL&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=42.0044757&longitude=-87.73005940000002&defaultZoomLevel=11",
"https://turo.com/search?location=Des%20Plaines%2C%20IL%2C%20USA&locationType=City&startDate=04%2F23%2F2017&startTime=10%3A00&endDate=04%2F30%2F2017&endTime=10%3A00&region=IL&country=US&category=ALL&instantBook=false&customDelivery=false&maximumDistanceInMiles=30&sortType=RELEVANCE&isMapSearch=false&latitude=42.0333623&longitude=-87.88339909999999&defaultZoomLevel=11",
]

for locationLink in AllLinks: 
	chrome_path = r"C:\Users\Shareef\Desktop\chromedriver.exe" #change path to browser here
	driver = webdriver.Chrome(chrome_path)
	driver.get(locationLink)
	driver.implicitly_wait(10)
	links = driver.find_elements_by_xpath("""//*[@id="results"]/ol/li/a""")

	for link in links:
		Mylink =  link.get_attribute('href')
		array = Mylink.split("/")
		carType =  array[4]
		source = urllib2.urlopen(Mylink).read()
		soup = bs.BeautifulSoup(source,'lxml')

		##Car And Owners Name
		basicInfo = []
		results = soup.find('div', {"class":"vehicleListingSummary-vehicleInformation"})
		for entry in results.contents:
			try:
				string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
				if string.encode("utf-8")[:1].isalpha():
					basicInfo.append(string.encode("utf-8"))
			except AttributeError:
				pass
		del basicInfo[0]
		allInfo = ";".join(basicInfo)

		##Number of Trips
		trips = "0 TRIPS"
		if soup.find('div', {"class" : "vehicleModelAndOwner-trips rating--trips"}):
			entry =  soup.find('div', {"class" : "vehicleModelAndOwner-trips rating--trips"})
			string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
			trips = string.encode("utf-8")

		##Location
		try:
			if soup.find('div', {"class":"u-inlineBlock hasIcon"}):
				entry =  soup.find('div', {"class":"u-inlineBlock hasIcon"})
				string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
				location = string.encode("utf-8")
			elif soup.find('div', {"class":"u-inlineBlock "}):
				entry =  soup.find('div', {"class":"u-inlineBlock "})
				string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
				location = string.encode("utf-8")
			elif soup.find('span', {"class", "js-reservationBoxLocationCurrentText reservationBoxLocationCurrentText-currentText"}):
				entry =  soup.find('div', {"class":"js-reservationBoxLocationCurrentText reservationBoxLocationCurrentText-currentText"})
				string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
				location = string.encode("utf-8")
		except AttributeError:
			pass
		
		##Car Features
		features = []
		results = soup.find_all('div', {"class":"basicCarDetails-label"})
		for entry in results:
			try:
				if entry.text.encode("utf-8"):
					string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
					features.append(string.encode("utf-8"))
			except AttributeError:
				pass

		results = soup.find_all(class_="u-tableCell u-verticalAlignMiddle")
		for entry in results:
			try:
				if entry.text.encode("utf-8"):
					string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
					features.append(string.encode("utf-8"))
			except AttributeError:
				pass
		allFeatures = ";".join(features)
		
		##Price
		results = soup.find('span', {"class", "vehicleListingSummary-dollars js-vehicleListingDailyAverage"})
		price = results.text.encode("utf-8") + "$"

		##Miles included
		try:
			entry = soup.find('div', {"class", "js-reservationBoxMileageDistance"})
			string = EntitySubstitution.substitute_html(entry.get_text().strip().upper())
			miles = string.encode("utf-8")
		except AttributeError:
			pass

		##Ratings 
		if soup.find('div', {"class":"stars r35 stars--purple"}):
			stars =  "3.5"
		if soup.find('div', {"class":"stars r40 stars--purple"}):
			stars =  "4" 
		if soup.find('div', {"class":"stars r45 stars--purple"}):
			stars = "4.5"
		if soup.find('div', {"class":"stars r50 stars--purple"}):
			stars = "5"

		## Owner link
		results = soup.find('div', {'class', 'driverDetails-name u-truncate'})
		dLink =  "https://turo.com" + results.contents[1]['href']
		try:
			miniLink = urllib2.urlopen(dLink).read()
			minisoup = bs.BeautifulSoup(miniLink,'lxml')
			results = minisoup.find('div', {'class','profile-join-date'})
			joinDate = results.text.strip().encode('utf-8')
			date = joinDate.split()
			date = ";".join([date[1],date[2]])
			##Driver Name
			name = minisoup.find('h2', {'class','profile-name'}).text.strip()
		except Exception, e:
			date = "NOT FOUND"
			name = "NOT FOUND"
			continue

		##Response Rate & %
		ResponseRate = "NA";
		ResponsePercent = "NA";
		try:
			results = soup.find_all('span', {'class', 'u-pullRight'})
			if results:
				try:
					ResponseRate = results[0].get_text().encode('utf-8')
					ResponsePercent = results[1].get_text().encode('utf-8')
				except IndexError:
					pass
		except AttributeError:
			pass

		## Description
		results = soup.find_all('div', {'class', 'js-description vehicleDescription vehicleDescription--large'})
		Description = str(results).replace("<","").replace(">","").replace("\\","").replace("/","")
		try:
			print "\t".join([name,allInfo,trips,location,allFeatures,price,miles,stars,date,ResponseRate,ResponsePercent,Description,carType])
		except Exception, e:
			print "NOT FOUND"
			continue
	driver.quit()