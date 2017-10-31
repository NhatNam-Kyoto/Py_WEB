import requests


while True:
    url =raw_input('url:')
    r = requests.get(url)
    code = r.status_code
    if code == 200:
        print 'Connect OK'
    else Error:
        print 'Not F0und'
    if url == 'exit':
        break
    pass
