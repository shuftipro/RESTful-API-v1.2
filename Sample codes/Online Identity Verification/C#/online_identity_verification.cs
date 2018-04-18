using (var client = new WebClient())
{
	var postData = new NameValueCollection();

	postData["client_id"]     = "YOUR CLIENT ID PROVIDED BY SHUFTIPRO";
	postData["reference"]     = "Your unique request reference";
	postData["email"]         = "customer email";
	postData["phone_number"]  = "+440000000000";
	postData["country"]       = "Pakistan";
	postData["lang"]		  = "2 digits code of supported languages for intarface language";]
	postData["callback_url"]  = "A valid callback url e.g https://www.yourdomain.com";
	postData["redirect_url"]  = "A valid callback url e.g https://www.yourdomain.com";

	var sericesData = new NameValueCollection();	
		sericesData["document_type"]        = "passport";
		sericesData["document_id_no"]       = "123-ABC-001";
		sericesData["document_expiry_date"] = "2025-01-01";
		sericesData["address"]              = "your address";
		sericesData["first_name"]           = "Nawaz";
		sericesData["last_name"]            = "Sharif";
		sericesData["dob"]                  = "1949-12-25";
		sericesData["background_checks"]    = "0";

	var jsonServicesData = JsonConvert.SerializeObject(sericesData);

	postData["verfication_services"]    = jsonServicesData;	

	string rawData="";
		//Sort the All request data to calculate signature
		foreach (var item in postData.AllKeys.OrderBy(k => k))
		{
			rawData +=postData[item];
		}
		//Append the secret key in the end
		rawData = rawData+"YOUR SECRET KEY";
		//get sha256 hash for signature value by using the below function
		string hash = GetHashSha256(rawData);
		
		postData["signature"] = hash;

		//send the request to shuftipro
		var response = client.UploadValues("https://api.shuftipro.com", postData);
		var responseString = Encoding.Default.GetString(response);

		//print your response here
		//If want to parse the JSON response uncomment the below lines
		//dynamic stuff = JObject.Parse(responseString);
		//string URL = stuff.message;

}

public static string GetHashSha256(string strData)
{
	var message = Encoding.ASCII.GetBytes(strData);
	SHA256Managed hashString = new SHA256Managed();
	string hex    = "";
	var hashValue = hashString.ComputeHash(message);
	
	foreach (byte x in hashValue)
	{
		hex += String.Format("{0:x2}", x);
	}
	return hex;
}