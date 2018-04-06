#!/usr/bin/python import hashlib import requests import  json
import collections

url = 'https://api.shuftipro.com/
CLIENT_ID = 'Your client id provided by Shuftipro' SECRET_KEY = 'YOUR_SECRET_KEY'

post_data = {
"method"              : "id_card OR passport OR driving_license",
"client_id"           : CLIENT_ID, "card_first_6_digits" : "123456", "card_last_4_digits"  : "7890",
"reference"           : "Your unique request reference", "country"             : "Pakistan",
"phone_number"        : "+440000000000",
"redirect_url"        : "A valid callback url e.g https://www.yourdomain.com", "face_image"          : "base64 of your face image (only required if you want to verify
	through still images (maximum size is 4mb))must provide the next 
parameter i.e document_image",
"document_image"      : "base64 of your document (id_card, passport, driving_license) 
(maximum size is 4mb)",
"video"               : "base64 of video, if you want to verify through offline video
verification" (maximum size is 8mb)

}



post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary response = requests.post(url, post_data).json() #send POST request to API

if response['status_code'] == "SP2":
print response['message']   #now you can redirect your customer to this url
