import dateutil.parser
import dateutil.rrule
import datetime
import time
import urllib2
from bs4 import BeautifulSoup
import numpy as np

base_url = "http://www.ncaa.com/scoreboard/basketball-men/d2/{}/{:02}/{:02}/all-conf"

header = {
	'User-Agent': 'Wget/1.17.1 (linux-gnu)',
	'Accept': '*/*',
	'Accept-Encoding': 'identity',
	'Host': 'www.ncaa.com',
	'Connection': 'Keep-Alive'}

def download(start = None, end = None):	
	data = []

	try:
		start = dateutil.parser.parse(start)
	except AttributeError:
		raise Exception('Start date not defined.')
	try:
		end = dateutil.parser.parse(end)
	except AttributeError:
		end = datetime.datetime(*time.localtime()[:6])

	for date in dateutil.rrule.rrule(dateutil.rrule.DAILY, dtstart = start, until = end):
		try:
			url = base_url.format(date.year, date.month, date.day)
			request = urllib2.Request(url, headers = header)
			print "Downloading {} ...".format(url),
			web = urllib2.urlopen(request)
			page = web.read()
			web.close()
			print "done"
		except urllib2.HTTPError:
			print "No games this day."
			continue
		soup = BeautifulSoup(page, "lxml")
		scoreboard = soup.find(id = "scoreboard").find_all("section")[1:]
		print "Found {} games".format(len(scoreboard))
		for game in scoreboard:
			scores = 2 * [None]
			teams = 2 * [None]
			try:
				for i in range(2):
					scores[i] = int(game.find_all(class_ = "final score")[i].string)
					teams[i] = game.find_all(class_ = "team")[i].a.string.encode('ASCII', 'ignore')
			except TypeError:
				print "No points listed for this game."
				continue
			winner = np.argmax(scores)
			data.append([teams[winner], teams[int(not bool(winner))]])
	return data
