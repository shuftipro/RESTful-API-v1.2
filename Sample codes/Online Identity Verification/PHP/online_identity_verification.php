<?php
$url        = "https://api.shuftipro.com/";
$client_id  = "Your client id provided by Shufti Pro";
$secret_key = 'YOUR_SECRET_KEY'; //Replace with your secret key provided by the Shufti Pro.

$verification_services = array(
	"document_type"        => "passport OR id_card OR driving_license OR null",
	"document_id_no"       => "123-ABC-001",
	"document_expiry_date" => "2025-01-01",
	"address"              => "your address",
	"first_name"           => "Nawaz",
	"last_name"            => "Sharif",
	"dob"                  => "1949-12-25",
	"background_checks"    => "0"
);
//JSON encode the services array
$verification_services = json_encode($verification_services);

$post_data = array(
	"client_id"            => $client_id,
	"reference"            => "Your unique request reference",
	"email"                => "customer email",
	"phone_number"         => "+440000000000",
	"country"              => "Pakistan",
	"lang"				   => "2 digits code of supported languages for intarface language"
	"callback_url"         => "A valid callback url e.g https://www.yourdomain.com", 
	"redirect_url"         => "A valid callback url e.g https://www.yourdomain.com",
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
?>