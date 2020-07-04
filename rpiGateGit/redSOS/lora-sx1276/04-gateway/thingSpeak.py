import sys
import urllib.request as urllib2
from time import sleep

myAPI = 'Q7ECDLD3HRHKS6W4'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
	try:
		conn = urllib2.urlopen(baseURL + '&field1=1')
		print(conn.read())
		conn.close()
		sleep(20)
		conn = urllib2.urlopen(baseURL + '&field1=0')
		print(conn.read())
		conn.close()
		sleep(20)
	except:
		print('Error')
		break
