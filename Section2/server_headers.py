import requests
url = 'http://httpbin.org/ip'
r = requests.get(url)
print 'Status code'
print '\t' + str(r.status_code) + '\n'
print '*************************************\n'
for x in r.headers:
	print '*\t' + x + ':' + r.headers[x]
print '*************************************\n'
print 'Content: '
print r.text