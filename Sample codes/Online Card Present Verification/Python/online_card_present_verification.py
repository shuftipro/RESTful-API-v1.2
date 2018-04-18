import hashlib 
import requests 
import json
import collections
from decimal import Decimal

url = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro'
SECRET_KEY = 'YOUR_SECRET_KEY'


verification_services ={}
verification_services["document_type"]        = "passport OR id_card OR driving_license OR null"
verification_services["document_id_no"]       = "123-ABC-001"
verification_services["document_expiry_date"] = "2025-01-01"
verification_services["address"]              = "your address"
verification_services["card_first_6_digits"]  = "123456"
verification_services["card_last_4_digits"]   = "7890"
verification_services["background_checks"]    = "0"

#json encode vericiation services
json_verification_services = json.dumps(verification_services, ensure_ascii=False)


post_data = {
"client_id"             : CLIENT_ID,
"reference"             : "Your unique request reference",
"email"                 : "customer email",
"phone_number"          : "+440000000000",
"country"               : "Pakistan",
"lang"                  : "2 digits code of supported languages for intarface language"
"callback_url"          : "A valid callback url e.g https://www.yourdomain.com", 
"redirect_url"          : "A valid callback url e.g https://www.yourdomain.com",
"verification_services" : json_verification_services  
}

post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary response = requests.post(url, post_data).json() #send POST request to API

if response['status_code'] == "SP2":
print response['message']   #now you can redirect your customer to this url
