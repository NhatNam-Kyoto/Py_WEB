import requests
url = 'http://natas4.natas.labs.overthewire.org/redirect-to'
payload = {'url':'http://natas5.natas.labs.overthewire.org/'}
r = requests.get(url)
print r.status_code
for x in r.headers:
	print x + ':' +r.headers[x]