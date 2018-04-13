<?php
$url="https://api.shuftipro.com/";


$verification_services = array(
	"document_type"        => "passport",
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

$verification_data = array(
	"face_image"             => "base64 of your face image (only required if you want to verify through still images (maximum size is 4mb)) must provide the next parameter i.e document_image",
	"document_front_image"   => "base64 of your document front image (maximum size is 4mb)",
	"document_back_image"    => "base64 of your document back image (maximum size is 4mb)",
	"document_address_image" => "base64 of your document address image (maximum size is 4mb)",
	"video"                  => "base64 string of video, if you want to verify through offline video verification (maximum size is 8mb)"
);
//JSON encode the services array
$verification_data = json_encode($verification_data);


$post_data = array(
	"client_id"             => $client_id,
	"reference"             => "Your unique request reference",
	"email"                 => "customer email",
	"phone_number"          => "+440000000000",
	"country"               => "Pakistan",
	"lang"                  => "2 digits code of supported languages for intarface language"
	"callback_url"          => "A valid callback url e.g https://www.yourdomain.com", 
	"redirect_url"          => "A valid callback url e.g https://www.yourdomain.com",
	"verification_services" => $verification_services, 
	"verification_data"     => $verification_data,
);

ksort($post_data);//Sort the all request parameter.
$raw_data = implode("", $post_data) . "YOUR_SECRET_KEY"; //Replace with your secret key provided by the Shuftipro;

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