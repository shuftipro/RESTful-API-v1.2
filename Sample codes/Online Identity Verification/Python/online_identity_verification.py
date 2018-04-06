#!/usr/bin/python import hashlib  import requests import  json
import collections

url = 'https://api.shuftipro.com/'
CLIENT_ID = 'Your client id provided by Shuftipro' SECRET_KEY = 'YOUR_SECRET_KEY'

post_data = {
"method"              : "passport OR id_card OR driving_license OR null" "client_id"           : CLIENT_ID,
"first_name"          : "John", "last_name"           : "Doe",
"dob"                 : "1980-01-31",
"reference"           : "Your unique request reference", "country"             : "United Kingdom",
"phone_number"        : "+440000000000",
"callback_url"        : "https://www.yourdomain.com",
"redirect_url"        : "https://www.yourdomain.com",
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
if response['status_code'] == "SP2":
print response['message']   #now you can redirect your customer to this url