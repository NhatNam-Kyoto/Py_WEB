import requests
import urllib
payload = {'url':'http://www.edge-security.com'}
r = requests.get('http://httpbin.org/redirect-to',params = payload)
s = urllib.urlopen('http://httpbin.org')
print s.read
#print 'Status code:'
#print '\t *' + str(r.status_code)
