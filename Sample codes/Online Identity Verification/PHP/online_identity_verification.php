<?php
$url= "https://api.shuftipro.com/";
$client_id = "Your client id provided by Shufti Pro";
$secret_key = 'YOUR_SECRET_KEY'; //Replace with your secret key provided by the Shufti Pro.

$post_data = array(
	"method"             => "id_card OR passport OR driving_license OR null", 
	"client_id"           => $client_id,
	"first_name"          => "John",
	"last_name"           => "Doe",
"dob"                 => "1980-01-31", //Customer date of birth in valid date format
"reference"           => "Your unique request reference", "country"             => "Pakistan",
"phone_number"        => "+440000000000",
"callback_url"        => "A valid callback url e.g https://www.yourdomain.com", "redirect_url"        => "A valid callback url e.g https://www.yourdomain.com",
);

ksort($post_data);//Sort the all request parameter.
$raw_data = implode("", $post_data) . $secret_key; 

$signature              = hash("sha256", $raw_data);
$post_data["signature"] = $signature;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url); curl_setopt($ch, CURLOPT_POST, 1); curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);
?>