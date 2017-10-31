import requests
url = 'http://httpbin.org/redirect-to'
payload = {'url':'https://www.google.com'}
r = requests.get(url,params = payload)
print 'http code:' + str(r.status_code) + '\n'
for x in r.history:
	print str(x.status_code) + ':' + x.url
