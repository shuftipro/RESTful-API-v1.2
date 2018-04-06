<?php
$url="https://api.shuftipro.com/";

$post_data = array(
	"method"              => "id_card OR passport OR driving_license OR null",
	"client_id"           => "Your client id provided by Shuftipro",
	"first_name"          => "John", "last_name"           => "Doe",
"dob"                 => "1980-01-31", //Customer date of birth in valid date format
"reference"           => "Your unique request reference", "country"             => "Pakistan",
"phone_number"        => "+440000000000",
"redirect_url"        => "A valid callback url e.g https://www.yourdomain.com", "face_image"          => "base64 of your face image (only required if you want to
	verify through still images (maximum size is 4mb)) must provide 
the next parameter i.e document_image",
"document_image"      => "base64 of your document (id_card, passport, driving_license) 
(maximum size is 4mb)",
"video"               => "base64 string of video, if you want to verify through offline
video verification" (maximum size is 8mb)
);

ksort($post_data);//Sort the all request parameter.
$raw_data = implode("", $post_data) . "YOUR_SECRET_KEY"; //Replace with your secret key provided by the Shuftipro;

$signature              = hash("sha256", $raw_data);
$post_data["signature"] = $signature;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url); curl_setopt($ch, CURLOPT_POST, 1); curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);
?>