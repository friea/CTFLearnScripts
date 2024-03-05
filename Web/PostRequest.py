import requests
url = "http://165.227.106.113/post.php"
data = {"username":"admin","password":"71urlkufpsdnlkadsf"}
session = requests.Session()
packet = session.post(url,data)
print(packet.text)