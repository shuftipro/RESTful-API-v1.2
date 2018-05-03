const qs = require("querystring");
const http = require("https");
const crypto = require('crypto');

const API_URL        = "api.shuftipro.com";
const CLIENT_ID  = "YOUR CLIENT ID";
const SECRET_KEY = 'YOUR SECRET KEY'; //Replace with your secret key provided by the Shufti Pro.

verification_services = {
	document_type: "passport",
	document_id_no: "123-ABC-001",
	document_expiry_date: "2025-01-01",
	address: "House 1, Street 10, London AL5 ABC, United Kingdom",
	first_name: "Robert",
	last_name:"Dickerson",
	dob:"1949-12-25",
	background_checks: "0"
};


post_data = {
	client_id: CLIENT_ID,
	reference: "ref-" + Math.floor(Math.random()*9999999999999),
	email: "customer@gmail.com",
	phone_number: "+440000000000",
	country: "gb",
	lang: "en",
	callback_url: "http://example.com",
	redirect_url: "http://example.com",
	verification_services: JSON.stringify(verification_services), //JSON encoded array
};


//Sort all the request parameters by their key and concatenate their values
var raw_data = "";
Object.keys(post_data).sort().forEach(function(v){
  raw_data += post_data[v];
});

//Append Secret Key at the endn
raw_data += SECRET_KEY;

post_data["signature"]              = crypto.createHash('sha256').update(raw_data, 'utf8').digest("hex")

var options = {
  "method": "POST",
  "hostname": API_URL,
  "path": "/",
  "headers": {
    "content-type": "application/x-www-form-urlencoded"
  }
};

var req = http.request(options, function (res) {
  var chunks = [];
  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    handle_api_response(body);
  });
});

req.write(qs.stringify(post_data))
req.end();

function handle_api_response(responseBody){
    //Parse Response body
    response = JSON.parse(responseBody);
    //Verify Response signature
    my_signature = crypto.createHash('sha256').update(response.status_code + response.message + response.reference + SECRET_KEY, 'utf8').digest("hex");

    if(my_signature == response.signature){
    		//Response is valid. Now you can redirect your customer if you receive status code SP2
    		if(response.status_code == "SP2"){
    			console.log("Redirect to: " + response.message);
    		}
    		else{
    			console.error(response.message);
    		}
    }
    else{
      	console.error("Response signature is invalid");
    }
}
