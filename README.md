[![](https://raw.githubusercontent.com/shuftipro/ShuftiProSDK/master/shufti_pro_sdk.png)](https://www.shuftipro.com/)
# Table of contents
* [Introduction](#introduction)
  * [Real-Time Verification](#real-time-verification)
  * [Offline Verification](#offline-verification)
* [Identity Verification](#identity-verification)
  * [General Purpose](#general-purpose)
  * [Driving License](#driving-license)
  * [Passport](#passport)
  * [ID Card](#id-card)
  * [RESTful Request](#restful-request)
* [Get Request status](#get-request-status)
* [Responses](#responses)
* [Status Codes](#status-codes)
* [Signature Calculation](#signature-calculation)
  * [Request Signature](#request-signature)
  * [Response Signature](#response-signature)
* [Sample Codes](#sample-codes)
* [Supported Languages](#supported-languages)
* [Test IDs](#test-ids)
* [Revision history](#revision-history)



# Introduction
Shufti Pro provides two modes of verification:
1. **Real-Time Verification**
2.	**Offline Verification**

In **Real time verification**, your customer has to show their face and the required document in front of the camera. On the other hand in **Offline Verification**, you have an opportunity to provide your customer’s identity document to us via this API and we’ll send you the verification results back.

### *Real-Time Verification*
A typical real-time verification workflow looks like this:
1.  You send us your customer’s data to verify at one of our end points. We validate your request  and  send  you  a  redirect  URL  so  you  can  redirect  your  customer  to  our verification page or you can embed this in an iFrame.
2.  Your customer sees an instruction page. Upon clicking ‘Next’ , the verification process starts.
3.  Your customer shows their face followed by the required document to the camera and the verification process begins in the background.
4.  Upon verification, your customer will be redirected back to the given URL. Along with this
URL, we’ll also send you the verification response via a callback.
5.  When  you  receive  a  verification  response  from  us,  you  will  also  receive  a  field **Signature**. You need to verify this field before proceeding further. An example is given below.

### *Offline Verification*
In this mode, you only make a single call to our API with your customer’s Identity document and we send you the verification result back in response to this API call. You can provide us this identity document either as an image or you can ask your customer to provide you a recorded video which you can forward to us. So for the Offline verification you can choose following methods:

1.  Still Image Verification (Your customer’s face and document image as a Base64 String)*
2.  Video Verification (A recorded video of your customer showing his/her face and identity document (details showing clearly in the camera))** <br>

*&nbsp; Base64 string size shouldn’t be greater than 4MB for each image <br>
** This video size shouldn’t be greater than 8MB

# Identity Verification
The Identity verification supports the following kinds of verification:
*   General Purpose verification
*   Driving license verification
*   Passport verification
*   ID Card verification

### *General Purpose*
Your customer is provided with a list of verification methods to choose from such as passport, driving license or ID card. After the user chooses one particular verification type, they are requested to display the required document in front of the camera. The validity of this document will make sure after cross checking the information provided in the request with that in the document

### *Driving License*
Your customer needs to display their Driving License. Shufti Pro verifies the validity of the driving license by cross checking the information (customer’s name and date of birth) provided in the request with that in the driving license.

### *Passport*
Your customer needs to display their passport. The validity of the passport is verified by cross checking the provided information with that in the passport. For example, the customer’s name and date of birth are cross checked to make sure whether the passport shown is forged or authentic.

### *ID Card*
Your customer needs to display their Identity Document. It could be government, school and/or university issued ID card. Shufti Pro verifies the validity of such ID card by cross checking the information (customer name and date of birth) provided in the request with that in the ID card.

### *RESTful Request*
You can make a request at the following endpoint with all the parameters defined below <br>
**Endpoint:**  	POST https://api.shuftipro.com/ <br>
**Format:**	    x-www-form-urlencoded

| Parameter | Online | Offline | Description |
| ------ | ------ | ------ | ------ |
| client_id | Required | Required | Client’s ID  provided by Shufti Pro to you. |
| reference | Required | Required | Your  Unique reference ID, which we will send you back with each response , so you can verify the request. Only alfa and num values are allowed. |
| email | Optional | Optional | The customer email. This parameter is to use if the verification result is pending or late then upon verification process completion; an email will be send to customer to notify his/her verification status. The verification result will be send to customer only if you provide the email. |
| phone_number | Required | Required | Customer’s phone number with country code. Example: +440000000000 |
| lang | Optional | Optional | Send ISO639-1 language code of your preferred language to display the verification screens accordingly. Please see the supported languages in this section. If this parameter is not sent then by default English as language will be displayed. |
| callback_url | Required | Optional | Upon every request, we make a server to server call, it includes all the response values, so you   can  update status on your end even if the customer is lost in the midway through the process. Please verify the response’s signature value  with your own calculated signature value.<br> **Remember:** It is not required if the user provides face_image, document_image or video. |
| redirect_url | Required | Required | Once the verification process is completed, we will redirect the customer  back  to your  given  URL.  In this  redirect request, you’ll also get all the response   values   in HTTP POST, so you can make your decision. Please verify the response’s signature value with your own calculated signature value. |
| verifcation_services | Required | Required | The JSON encoded array of all data which is required to verify. The all data to verify will be send in this parameter. The key will be name of service which you want to verify e.g dob, first_name etc.<table> <tr> <td>document_type</td> <td>Which type of verification would you like for your   customers? <br> Possible   values: <br> <ul><li> passport </li><li> driving_license </li><li> id_card</li></ul> In real time verification if an empty value is provided then the end user will have an option to choose any of the verification method from the list given</td> </tr> <tr> <td>document_id_no</td> <td>The valid ID number of your document</td> </tr> <tr> <td>document_expiry_date</td> <td>The expiry date  of customer's document. Example: 2025-01-31</td> </tr> <tr> <td>address</td> <td>customer's address on the document or utility bill</td> </tr> <tr> <td>first_name</td> <td>Customer’s First Name on the document</td> </tr> <tr> <td>last_name</td> <td>Customer’s Last Name. on the document</td> </tr> <tr> <td>dob</td> <td>Customer’s date of birth (YYYY-MM-DD). Example: 1980-01-31</td> </tr> <tr> <td>card_first_6_digits</td> <td>First 6 digits of the customer’s credit/debit card number if document type is debit/credit</td> </tr> <tr> <td>card_last_4_digits</td> <td>Last 4 digits of the customer’s credit/debit card number if document type is debit/credit</td> </tr> <tr> <td>background_checks</td> <td>Send 1 or 0 (Boolean) value. If you want to check the background details of the customer send this key with value 1</td> </tr> </tr> </table> |
| verification_data | Optional  | Required | <table><tr> <td>face_image</td> <td>The base 64 string of the face. If the user wants to verify themselves through offline   verification (still images) (Max size 4MB allowed)</td> </tr> <tr> <td>document_front_image</td> <td>The base 64 string of the document mentioned  in “document_type” parameter (passport, driving_license, id_card) (Max size 4MB allowed)</td> </tr> <tr> <td>document_back_image</td> <td>The base64 string of the customer’s document back side image.(if any) (Max size 4MB allowed)</td> </tr> <tr> <td>document_address_image</td> <td>he base64 string of the customer's utility bill or any document which must contain the residence address. If you want to verify the address then please send this image too. (Max size 4MB allowed)</td> </tr> <tr> <td>video</td> <td>The  base  64  of the video is only required when the user wants to verify him/herself through offline verification (by sending video) (Max size 8MB allowed)</td> </tr> </table> |
| signature | Required | Required | SHA256 hash of all the request parameters in sorted order. The details are in the signature calculation section. |


#  Get Request status
To get the request status later after verification you may use this endpoint. To get the request status you are required to send the client_id, reference and signature in POST request. The reference is your unique request **reference** which you send at the time of request. Calculate the signature as described in signature calculation section. If all the validation passed and your request is found in our record then you will get back the verification status of request which is associated with the reference you are providing. <br>

**Endpoint:**  	POST https://api.shuftipro.com/status <br>
**Format:**	    x-www-form-urlencoded

| Parameter | Required | Description |
| ------ | ------ | ------ |
| client_id | Yes | Client’s ID provided by Shufti Pro to you. (ID must be in alphanumeric format) |
| reference | Yes | Your unique request reference which you have send at the time of request. (a valid request reference which is associated with  any request at the time of request) |
| signature | Yes | Concat request values as client_id, reference and secret_key, then calculate SHA256 hash of all values. |

Find sample codes under this section.

# Responses
The Shufti Pro API will send you two types of responses. First is the HTTP response sent against your request, and the second is the callback response, respectively. Both HTTP and callback responses will be in the JSON format and they will contain the following parameters:

| Parameter | Description |
| ------ | ------ |
| status_code | One of the status codes from the status codes section. |
| message | The description of status code. If the status code is **SP2** then the message will be a redirect URL. |
| reference | Your unique request reference which was provided at the time of request so that you can identify the response in relation to request made. |
| signature | The **SHA256** hash of all response parameters. The process of signature calculation is given in the response signature calculation section. |


> **Note:** Callback response will be sent on the callback_url provided in the request **callback_url** parameter


# Status Codes
Status codes represent the status of the verification process (Success / Failure). The Shufti Pro Verification API uses the following status codes sent throughout when making any kind of verification request.

| Status Code | Description | HTTP | Callback |
| ------ | ------ | ------ | ------ |
| SP0 | Not Verified | Yes | Yes |
| SP1 | Verified | Yes | Yes |
| SP2 | Success! -- Contains the redirect url in message parameter. | Yes | Yes |
| SP11 | Length Validation -- [parameter_name] maximum and minimum length limit is [min & max] characters. | Yes | Yes |
| SP14 | Duplicate reference -- If a duplicate reference is provided. | Yes | Yes |
| SP15 | Invalid client id -- Client id is invalid or not found. | Yes | Yes |
| SP16 | Missing required parameter -- ["parameter_name"] is required but either missing or empty | Yes | Yes |
| SP17 | Invalid format -- ["parameter_name"] is  not  in the correct format. | Yes | Yes |
| SP18 | Invalid signature -- Invalid request signature. | Yes | Yes |
| SP19 | Invalid country code -- Invalid country code or country is not supported. | Yes | Yes |
| SP20 | Invalid Phone No -- Invalid phone number is provided. | Yes | Yes |
| SP21 | Invalid Method Name -- Given verification method is not supported. | Yes | Yes |
| SP22 | Invalid checksum value | Yes | Yes |
| SP23 | Invalid DOB -- Date of birth is not valid. | Yes | Yes |
| SP24 | Blocked Client -- Your account is not active. | Yes | Yes |
| SP25 | Request Timeout -- Sends  in  callback when request timeouts | Yes | Yes |
| SP26 | User has been landed on verification page | Yes | Yes |
| SP27 | Request is already processed | Yes | Yes |
| SP29 | Invalid size. The size limit for ["parameter_name"] is ["size in MBs"] | Yes | Yes |
| SP32 | Invalid request reference. Request not found | Yes | Yes |
| SP35 | [parameter_name] not allowed with [method_name] verification method | Yes | Yes |

# Signature Calculation
The request and response signature can be calculated as following: 
### *Request Signature*
1.  Sort all the request parameters (keys) in (ascending alphabetical order) 
and concatenate them.
2.  Append the secret key in the end.
3. Calculate the SHA256 hash of string (made in above 2  steps)

### *Response Signature*
1.  Decode the response from JSON format.
2.  Get all the response parameters’ values and concatenate them.
3.  Append the secret key in the end
4.  Calculate the SHA256 hash of the string (made in above 2  steps).

So for example if you have 3 following parameters and your secret key is **Trump**: <br>
```
first_name:	Alex 
last_name:	John 
dob:		1990-12-25 
You’d calculate its signature as 
SHA256 (“1990-12-25AlexJohnTrump”) = ea617383129f67037f369d2bc66c7e44a3690ddcf93f52128d828fdf3cab2b2c
```
Please note here, parameters are sorted ascendingly by their keys  as  **d**ob, **f**irst_name and **l**ast_name and then Secret Key at the end.

# Sample Codes
Below are the sample codes in php, python & c# for the following verification methods <br>
1.  [Online Identity verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Online%20Identity%20Verification)
2.  [Online Card Present verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Online%20Card%20Present%20Verification)
3.  [Offline Identity verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Offline%20Identity%20Verification)
4.  [Offline Card Present verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Offline%20Card%20Present%20Verification)

# Supported Languages
| Language | Code |
| ------ | ------ |
| Arabic | ar |
| English | en |
| Estonian | et |
| Russian | ru |
| Arabic     | ar |
| English    | en |
| Estonian   | et |
| Russian    | ru |
| Italian    | it |
| Turkish    | tr |
| Swedish    | sv |
| Spanish    | es |
| Romanian   | ro |
| Portuguese | pt |
| Korean     | ko |
| Polish     | pl |
| Norwegian  | no |
| Japanese   | ja |
| Icelandic  | is |
| French     | fr |
| German     | de |
| Dutch      | nl |
| Danish     | da |
| Indonesian | in |
| Chinese    | zh |

# Test IDs
Shufti Pro provides the users with a number of test documents. Customers may use these to test the demo, instead of presenting their actual information. <br><br>

Verification Result: “Verified” - Reason: Face Verified. <br>
[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg) <br>

Verification Result: “Not Verified“ - Reason: Face not Verified. <br>
[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/fakeFace.jpg)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/fakeFace.jpg) <br>

Verification Result: “Verified” - Reason: Information correctly detected | Name/DoB/Card Number matched. <br>
[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg) <br>

Verification Result: “Not Verified” - Reason: Incorrect information detected | Name/DoB/Card Number not matched.<br>
[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/fakeId.jpg)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/fakeId.jpg) <br>



# Revision history 
| Date | Version | Description |
| ------ | ------ | ------ |
| March 14, 2018 | 1.0.1 | Added new endpoint for get request status. https://api.shuftipro.com/status |
| March 26, 2018 | 1.0.1 | Added lang parameter & supported languages list |
| March 29, 2018 | 1.0.1 | Added C# sample codes |
| April 10, 2018 | 1.0.1 | Added new supported languages |



2016-18 © Shufti Pro Ltd.







