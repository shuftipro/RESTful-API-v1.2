using (var client = new WebClient())
{
	var postData = new NameValueCollection();

	postData["method"]              = "id_card";
	postData["client_id"]           = "YOUR ID";	
	postData["first_name"] 	   = "Test First Name";
	postData["last_name"]           = "Test Last Name";
	postData["dob"]          	   = "1990-01-01";
	postData["country"]             = "Sweden";
	postData["phone_number"]        = "+133458901";
	postData["reference"]           = "rf01-124750";
	postData["redirect_url"]        = "https://url.com/1fjmza31";
	postData["callback_url"]        = "https://url.com/1fjmza31";

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
		string hex = "";
		var hashValue = hashString.ComputeHash(message);
		
		foreach (byte x in hashValue)
		{
			hex += String.Format("{0:x2}", x);
		}
		return hex;
	}
