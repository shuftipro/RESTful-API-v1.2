using (var client = new WebClient())
{
	var postData = new NameValueCollection();

	postData["client_id"]           = "YOUR ID";	
	postData["reference"]           = "Your unique request reference";

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
		var response = client.UploadValues("https://api.shuftipro.com/status", postData);
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
