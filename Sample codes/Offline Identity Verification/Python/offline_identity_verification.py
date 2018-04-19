#!/usr/bin/python
import hashlib
import requests
import json
import collections
import random
import base64
import requests
from decimal import Decimal

url = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro'
SECRET_KEY = 'YOUR_SECRET_KEY'



verification_services ={}
verification_services["document_type"]        = "passport"
verification_services["document_id_no"]       = "6980XYZ4521XYZ"
verification_services["first_name"]           = "John"
verification_services["last_name"]            = "Doe"
verification_services["dob"]                  = "1900-01-01"
verification_services["background_checks"]    = "0"

#json encode vericiation services
json_verification_services = json.dumps(verification_services, ensure_ascii=False)

verification_data ={}

#Sample Face Image
sample_face_image = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg"
sample_id_image = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg"

verification_data["face_image"]             = base64.b64encode(requests.get(sample_face_image).content)
verification_data["document_front_image"]   = base64.b64encode(requests.get(sample_id_image).content)


#json encode vericiation data
json_verification_data = json.dumps(verification_data, ensure_ascii=False)

post_data = {
"client_id"             : CLIENT_ID,
"reference"             : "ref-" + str(random.randint(1000,10000)),
"email"                 : "customer@email.com",
"phone_number"          : "+440000000000",
"country"               : "it",
"lang"                  : "de",
"callback_url"          : "https://www.yourdomain.com",
"redirect_url"          : "https://www.yourdomain.com",
"verification_services" : json_verification_services,
"verification_data"     : json_verification_data
}

post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary
raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash
signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary
response = requests.post(url, post_data).json() #send POST request to API

#Validate response signature
my_signature = hashlib.sha256(response["status_code"] + response["message"]  +response["reference"] + SECRET_KEY).hexdigest()

if my_signature == response["signature"]:
    # Response is valid.
    print response["message"];
else:
    print "Response signature is invalid";
