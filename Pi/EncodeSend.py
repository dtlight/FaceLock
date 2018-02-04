import base64
from base64 import b64encode
import json
import requests
import urllib.request
image = open('image.jpg', 'rb')
image_read = image.read()
b64_bytes = base64.b64encode(image_read)
#print (image_64_encode)

b64_string = b64_bytes.decode('utf-8')

payload = {'img': b64_string}

body = {'img':b64_string}
myurl = "http://127.0.0.1:5000/pi"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
response = urllib.request.urlopen(req, jsondataasbytes)
