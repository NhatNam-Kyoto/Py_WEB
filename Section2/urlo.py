from urllib.request import urlopen

url = r'https://fptshop.com.vn/may-tinh-xach-tay/asus-fx553vd-dm304'
source = urlopen(url).read()
print(source)