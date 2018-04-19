import hashlib
import requests
import json
import collections
import random
from decimal import Decimal

url = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro'
SECRET_KEY = 'YOUR_SECRET_KEY'


verification_services ={}
verification_services["document_type"]        = "credit_card"
verification_services["card_first_6_digits"]  = "123456"
verification_services["card_last_4_digits"]   = "7890"
verification_services["background_checks"]    = "0"

#json encode vericiation services
json_verification_services = json.dumps(verification_services, ensure_ascii=False)


post_data = {
"client_id"             : CLIENT_ID,
"reference"             : "ref" + str(random.randint(1000,100000)),
"email"                 : "customer@email.com",
"phone_number"          : "+440000000000",
"country"               : "gb",
"lang"                  : "en",
"callback_url"          : "https://www.yourdomain.com",
"redirect_url"          : "https://www.yourdomain.com",
"verification_services" : json_verification_services
}

post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary
raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash
signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary


#send POST request to API
response = requests.post(url, post_data).json()

#Validate response signature
my_signature = hashlib.sha256(response["status_code"] + response["message"]  +response["reference"] + SECRET_KEY).hexdigest()

if my_signature == response["signature"]:
    # Response is valid. Now you can redirect your customer if you receive status code SP2
    if response["status_code"] == "SP2":
        print "Redirect to: " + response["message"];
    else:
        print response["message"];
else:
    print "Response signature is invalid";
