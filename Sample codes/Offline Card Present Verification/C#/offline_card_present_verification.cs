using (var client = new WebClient())
{
	var postData = new NameValueCollection();

	postData["method"]              = "credit_card";
	postData["client_id"]           = "YOUR ID";	
	postData["card_first_6_digits"] = "123456";
	postData["card_last_4_digits"]  = "7890";
	postData["country"]             = "Sweden";
	postData["phone_number"]        = "+133458901";
	postData["reference"]           = "rf01-124750";
	postData["redirect_url"]        = "https://url.com/1fjmza31";
	postData["callback_url"]        = "https://url.com/1fjmza31";
	postData["face_image"]          = "Base64 string of face image";
	postData["document_image"]      = "Base64 string of document image";

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
		//You will get verification result in the response in offline verficiation

	}

	public static string GetHashSha256(string strData)
	{
		var message = Encoding.ASCII.GetBytes(strData);
		SHA256Managed hashString = new SHA256Managed();
		string hex = "";
		var hashValue = hashString.ComputeHash(message);
		
		foreach (byte x in hashValue)
		{
			hex += String.Format("{0:x2}", x);
		}
		return hex;
	}
