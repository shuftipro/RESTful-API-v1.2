#!/usr/bin/python import hashlib import requests import  json
import hashlib 
import requests 
import json
import collections
from decimal import Decimal

url = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro' SECRET_KEY = 'YOUR_SECRET_KEY'

verification_services ={}
verification_services["document_type"]        = "passport OR id_card OR driving_license OR null"
verification_services["document_id_no"]       = "123-ABC-001"
verification_services["document_expiry_date"] = "2025-01-01"
verification_services["address"]              = "your address"
verification_services["first_name"]           = "Nawaz"
verification_services["last_name"]            = "Sharif"
verification_services["dob"]                  = "1949-12-25"
verification_services["background_checks"]    = "0"

#json encode vericiation services
json_verification_services = json.dumps(verification_services, ensure_ascii=False)

verification_data ={}
verification_data["face_image"]             = "base64 of your face image (only required if you want to verify through still images (maximum size is 4mb)) must provide the next parameter i.e document_image"
verification_data["document_front_image"]   = "base64 of your document front image (maximum size is 4mb)"
verification_data["document_back_image"]    = "base64 of your document back image (maximum size is 4mb)"
verification_data["document_address_image"] = "base64 of your document address image (maximum size is 4mb)"
verification_data["video"]                  = "base64 string of video, if you want to verify through offline video verification (maximum size is 8mb)"

#json encode vericiation data
json_verification_data = json.dumps(verification_data, ensure_ascii=False)

post_data = {
"client_id"             : CLIENT_ID,
"reference"             : "Your unique request reference",
"email"                 : "customer email",
"phone_number"          : "+440000000000",
"country"               : "Pakistan",
"lang"                  : "2 digits code of supported languages for intarface language",
"callback_url"          : "A valid callback url e.g https://www.yourdomain.com", 
"redirect_url"          : "A valid callback url e.g https://www.yourdomain.com",
"verification_services" : json_verification_services,
"verification_data"     : json_verification_data  
}

post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary 
raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash 
signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary 
response = requests.post(url, post_data).json() #send POST request to API

if response['status_code'] == "SP2":
  print response['message']   #now you can redirect your customer to this url
