#!/usr/bin/python
import hashlib, requests, json, collections, json, random
from decimal import Decimal

url       = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro'
SECRET_KEY = 'YOUR_SECRET_KEY'


verification_services ={}
verification_services["document_type"]        = "passport"
verification_services["document_id_no"]       = "123-ABC-001"
verification_services["document_expiry_date"] = "2025-01-01"
verification_services["address"]              = "House 1, Street 10, London AL5 ABC, United Kingdom"
verification_services["first_name"]           = "Robert"
verification_services["last_name"]            = "Dickerson"
verification_services["dob"]                  = "1949-12-25"
verification_services["background_checks"]    = "0"

#json encode vericiation services
json_verification_services = json.dumps(verification_services, ensure_ascii=False)


post_data = {
"client_id"             : CLIENT_ID,
"reference"             : "ref-" + str(random.randint(1000,100000)),
"email"                 : "customer@gmail.com",
"phone_number"          : "+440000000000",
"country"               : "gb",
"lang"                  : "en",
"callback_url"          : "http://example.com",
"redirect_url"          : "http://example.com",
"verification_services" : json_verification_services
}


#sort the dictionary
post_data = collections.OrderedDict(sorted(post_data.items()))

#get values from dictionary and append secret key
raw_data = "".join(post_data.values()) + SECRET_KEY

#calculate sha 256
signature = hashlib.sha256(raw_data).hexdigest()

#append signature to data dictionary
post_data['signature'] = signature

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
