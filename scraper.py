from datetime import date, timedelta
from time import strftime
import json
import urllib2, urllib

# Date we need in format DD.MM.YYYY, defaults is yesterday
yesterday = date.today() - timedelta(1)
date = yesterday.strftime("%d.%m.%Y")

# The page we need to scrape
url = "http://powietrze.katowice.wios.gov.pl/dane-pomiarowe/pobierz"

# The POST data we'll send
data = "query=%7B%22measType%22%3A%22Auto%22%2C%22viewType%22%3A%22Station%22%2C%22dateRange%22%3A%22Day%22%2C%22date%22%3A%22"+date+"%22%2C%22viewTypeEntityId%22%3A%223%22%2C%22channels%22%3A%5B36%2C44%2C61%2C41%2C49%2C60%2C51%2C52%2C39%2C62%2C43%2C46%2C66%5D%7D"

# Sends the request 
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

# Converts the response to JSON
response_json = json.loads(response.read())

# Parse the JSON to a CSV file
for series in response_json["data"]["series"]:
	series_id = series["paramId"]
	for data in series["data"]:

		# Bear in mind that data[0] is a UNIX epoch timestamp
		print series_id +","+data[0]+","+data[1]