'''
SIMPLE CODE GET SOURCE FROM WEB AND WRITE IT IN TXT FILE USING Requests .
'''

import requests
url = raw_input('URL: ')
r = requests.get(url)
f = open('soure.txt','w')

f.write(r.text.encode('utf8'))
f.close()
print 'Ghi Source thanh cong'
#print r.status_code
