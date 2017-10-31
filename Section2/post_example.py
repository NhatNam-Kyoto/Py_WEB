
import requests
url ='http://httpbin.org/post'
r = requests.post(url,{'name':'Nhatnam'})
print 'Status code:'
print '\t' + str(r.status_code) + '\n'
print '*************************************\n'
print 'Server header:'
for x in r.headers:
	print '\t' + x + ':' + r.headers[x]
print '************************************\n'
print 'Content:'
print r.text	