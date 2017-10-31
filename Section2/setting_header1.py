import requests
myheader = {'user-agent':'Nhatnam'}
url = 'http://httpbin.org/headers'
r = requests.get(url,headers = myheader)
print 'Status code:'
print '\t'+ str(r.status_code) + '\n'
print '******************************\n'
print 'Server header:'
for x in r.headers:
	print '\t' + x + ':' + r.headers[x]
print'*******************************\n'
print 'Content: '
print r.text 