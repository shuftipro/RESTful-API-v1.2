<?php
$url="https://api.shuftipro.com/status";
$post_data = array(
	"client_id"           => "Your client id provided by Shuftipro", 
	"reference"           => "Your unique request reference",
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