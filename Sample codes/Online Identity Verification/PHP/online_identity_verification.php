<?php
$url        = "https://api.shuftipro.com/";
$client_id  = "Your client id provided by Shufti Pro";
$secret_key = 'YOUR_SECRET_KEY'; //Replace with your secret key provided by the Shufti Pro.

$verification_services = array(
	"document_type"        => "passport",
	"document_id_no"       => "123-ABC-001",
	"document_expiry_date" => "2025-01-01",
	"address"              => "House 1, Street 10, London AL5 ABC, United Kingdom",
	"first_name"           => "Robert",
	"last_name"            => "Dickerson",
	"dob"                  => "1949-12-25",
	"background_checks"    => "0"
);
//JSON encode the services array
$verification_services = json_encode($verification_services);

$post_data = array(
	"client_id"            => $client_id,
	"reference"            => "ref-" . rand(1000,10000000),
	"email"                => "customer@gmail.com",
	"phone_number"         => "+440000000000",
	"country"              => "gb",
	"lang"				   			 => "en",
	"callback_url"         => "http://example.com",
	"redirect_url"         => "http://example.com",
	"verification_services" => $verification_services,

);

ksort($post_data);//Sort the all request parameter.
$raw_data = implode("", $post_data) . $secret_key;

$signature              = hash("sha256", $raw_data);
$post_data["signature"] = $signature;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);


#Parse Response body
$response = json_decode($response);

#Verify Response signature
$my_signature = hash("SHA256", $response->status_code . $response->message . $response->reference . $secret_key);

if($my_signature == $response->signature){
		# Response is valid. Now you can redirect your customer if you receive status code SP2
		if($response->status_code == "SP2"){
			header("Location: " . $response->message);
		}
		else{
			echo $response->message;
		}
}
else{
	echo "Response signature is invalid";
}

?>
