import hashlib 
import requests 
import  json
import collections

url = 'https://api.shuftipro.com/status'
CLIENT_ID = 'Your client id provided by Shuftipro'
SECRET_KEY = 'YOUR_SECRET_KEY'

post_data = {
"client_id"           : CLIENT_ID, 
"reference"           : "Your unique request reference", 
}


post_data = collections.OrderedDict(sorted(post_data.items())) #sort the dictionary raw_data = "".join(post_data.values()) + SECRET_KEY #get values from dictionary and append secret key

hash_object = hashlib.sha256(raw_data) #calculating sha 256 hash signature = hash_object.hexdigest()

post_data['signature'] = signature #append signature to data dictionary response = requests.post(url, post_data).json() #send POST request to API
