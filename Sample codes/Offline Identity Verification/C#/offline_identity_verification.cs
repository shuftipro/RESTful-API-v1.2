using (var client = new WebClient())
{
			
	var ApiURL    = "https://api.shuftipro.com/";
	var ClientId  = "Client Id provided by Shuftipro";
	var SecretKey = "Your Secret Key";//Replace with your secret key provided by the Shufti Pro.
			
	
	var VerficationServices =  new 
	{		
		document_type        = "passport",
		document_id_no       = "123-ABC-001",
		document_expiry_date = "2025-01-01",
		address              = "your address",
		first_name           = "John",
		last_name            = "Doe",
		dob                  = "1900-01-01",
		background_checks    = "0",
	};
		
		
	//JSON encode the service collection
	var JsonEncodedServices = JsonConvert.SerializeObject(VerficationServices);
		
	
	var SampleFaceImage = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg";
	var SampleIdImage   = "https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg";
			
	//Sample Images get and convert to Base64
	

	var VerficationData = new 
	{   
		face_image           = GetB64SampleDocImage(SampleFaceImage), 
		document_front_image = GetB64SampleDocImage(SampleIdImage)
	};

	var JsonEncodedVerificationData = JsonConvert.SerializeObject(VerficationData);
	
			
	var PostData = new NameValueCollection();

	PostData["client_id"]     =  ClientId;
	PostData["reference"]     = "sd-1198990";
	PostData["email"]         = "test@test.com";
	PostData["phone_number"]  = "+440000000000";
	PostData["country"]       = "US";
	PostData["lang"]		  = "en";
	PostData["callback_url"]  = "https://www.yourdomain.com";
	PostData["redirect_url"]  = "https://www.yourdomain.com";
	PostData["verification_services"] = JsonEncodedServices;		
	PostData["verification_data"]    = JsonEncodedVerificationData;	
	string RawData="";

	//Sort the All request data to calculate signature
	foreach (var item in PostData.AllKeys.OrderBy(k => k))
	{
		RawData += PostData[item];
	}
	//Append the secret key in the end
	RawData = RawData+SecretKey;
	
	//get sha256 hash for signature value by using the below function
	string hash = GetHashSha256(RawData);
	
	PostData["signature"] = hash;

	//send the request to shuftipro
		
	var Response = client.UploadValues(ApiURL, PostData);
	var ResponseString = Encoding.Default.GetString(Response);
	
	dynamic stuff = JObject.Parse(ResponseString);
	var ConcatenatedData = (string) stuff.status_code + stuff.message + stuff.reference + SecretKey;
	var MySignature = GetHashSha256(ConcatenatedData);
	if(MySignature == (string)stuff.signature){
		//Response is valid.
		//Get message key value as (string)stuff.message
	}
	else{
		//Response signature is invalid
	}

}
	
private static string GetHashSha256(string strData)
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

private static string GetB64SampleDocImage(string URL)
{
	System.Net.WebClient wc = new System.Net.WebClient(); 
	byte[] response = wc.DownloadData(URL); 	
	return Convert.ToBase64String(response);
}