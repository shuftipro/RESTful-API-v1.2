<?php
$url="https://api.shuftipro.com/";
$client_id  = "Your client id provided by Shufti Pro";
$secret_key = 'YOUR_SECRET_KEY'; //Replace with your secret key provided by the Shufti Pro.


$verification_services = array(
	"document_type"        => "passport",
	"document_id_no"       => "6980XYZ4821XYZ",
	"first_name"           => "John",
	"last_name"            => "Doe",
	"dob"                  => "1900-01-01",
	"background_checks"    => "0"
);
//JSON encode the services array
$verification_services = json_encode($verification_services);

$sample_face_image = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg";
$sample_id_image = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg";


$verification_data = array(
	"face_image"             => base64_encode(file_get_contents($sample_face_image)),
	"document_front_image"   => base64_encode(file_get_contents($sample_id_image))
);
//JSON encode the services array
$verification_data = json_encode($verification_data);


$post_data = array(
	"client_id"             => $client_id,
	"reference"             => "ref-" . rand(1000,100000),
	"email"                 => "customer@gmail.com",
	"phone_number"          => "+440000000000",
	"country"               => "us",
	"lang"                  => "en",
	"callback_url"          => "https://www.yourdomain.com",
	"redirect_url"          => "https://www.yourdomain.com",
	"verification_services" => $verification_services,
	"verification_data"     => $verification_data
);

ksort($post_data);//Sort the all request parameter.
$raw_data = implode("", $post_data) . $secret_key; //Replace with your secret key provided by the Shuftipro;

$signature              = hash("sha256", $raw_data);
$post_data["signature"] = $signature;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

$response = json_decode($response);
$my_signature = hash("SHA256", $response->status_code . $response->message . $response->reference . $secret_key);


if($my_signature == $response->signature){
		# Response is valid.
		echo $response->message;
}
else{
	echo "Response signature is invalid";
}
?>
