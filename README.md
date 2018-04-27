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
  * [How to make a verification request](#how-to-make-a-verification-request)
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
2.  Your customer sees an instruction page. Upon clicking ‘Next’, the verification process starts.
3.  Your customer shows their face followed by the required document to the camera and the verification process begins in the background.
4.  Upon verification, your customer will be redirected to the given URL. Along with this
URL, we’ll also send you the verification response via a callback. A callback is made before we redirect your customer to your redirect url.
5.  When you receive  a  verification  response  from  us,  you  will  also  receive  a  field **Signature**. You need to verify this field before proceeding further. An example is given  [here](#signature-calculation).

### *Offline Verification*
In this mode, you only make a single call to our API with your customer’s Identity document and we send you the verification result back in response to this API call. You can provide us with this identity document either as an image or you can ask your customer to provide you with a recorded video, which you can forward to us. Therefore, for the Offline verification you can choose following methods:

1.  Still Image Verification (Your customer’s face and document image as a Base64 String)*
2.  Video Verification (A recorded video of your customer showing their face and identity document (details showing clearly in the camera))** <br>

*&nbsp; Base64 string size shouldn’t be greater than 4MB for each image <br>
** This video size shouldn’t be greater than 8MB

# Identity Verification
The Identity verification supports the following kinds of verification:
*   General Purpose verification
*   Driving license verification
*   Passport verification
*   ID Card verification

### *General Purpose*
Your customer is provided with a list of ID documents to choose from such as passport, driving license or ID card. After the user chooses one particular document, they are requested to display the required document in front of the camera. The document's validity is ensured after cross checking the information provided in the request with that present on the document.

### *Driving License*
Your customer needs to display their Driving License. Shufti Pro verifies the validity of the driving license by cross checking the information (customer’s name and date of birth) provided in the request with that on the driving license.

### *Passport*
Your customer needs to display their passport. The validity of the passport is verified by cross checking the provided information with that on the passport. For example, customer’s name and date of birth are cross checked to judged whether the passport shown is forged or authentic.

### *ID Card*
Your customer needs to display their Identity Card. It could be government, school and/or university issued ID card. Shufti Pro verifies the validity of such ID card by cross checking the information (customer's name and date of birth) provided in the request with that on the ID card.

### *How to make a verification request*
You can make a request at the following endpoint with all the parameters defined below. <br>
**Endpoint:**  	POST https://api.shuftipro.com/ <br>
**Format:**	    x-www-form-urlencoded

| Parameter | Online | Offline | Description |
| ------ | ------ | ------ | ------ |
| client_id | Required | Required | Client’s ID  provided by Shufti Pro to you. |
| reference | Required | Required | Your  Unique reference ID, which we will send you back with each response, so you can verify the request. Only alphanumeric values are allowed. |
| email | Optional | Optional | This parameter is used to notify your customer in case a verification result is delayed. |
| phone_number | Required | Required | Customer’s phone number with country code. Example: +440000000000 |
| lang | Optional | Optional | Send [ISO639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code of your preferred language to display the verification screens accordingly. Please find a list of supported languages [here](#supported-languages).  |
| country | Required | Required | Send the 2 characters long [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country code of where your customer is from.  |
| callback_url | Required | Optional | During a verification request, we make several server to server calls to keep you updated about the verification state. These states include: i) Customer lands on our verification page; ii) Verification process completes. This way you can update the request status at your end even if the customer is lost midway through the process. |
| redirect_url | Required | Required | Once the verification process completes, we redirect your customer to your given URL. In this  redirect request, you’ll also get all the verification response values using HTTP POST method, so you can make your decision. Please verify the response’s signature value with your own calculated signature value. |
| verifcation_services | Required | Required | The JSON encoded array of all the data which you want us to verify using our different services. The key in this JSON encoded array will be the name of service which you want use in this verification request. e.g dob, first_name etc. All the available keys and the corresponding values are given below: <table> <tr> <td>document_type</td> <td>Which type of document would you like your customer to verify with? <br> Possible values: <br> <ul><li> passport </li><li> driving_license </li><li> id_card</li></ul> In [real time verification](#real-time-verification) if an empty value is provided then the end user will have an option to choose any of the verification method from the given list.</td> </tr> <tr> <td>document_id_no</td> <td>The valid ID number of your customer's identity document which you want us to verify. e.g. Passport number, ID card number and Driving License number. </td> </tr> <tr> <td>document_expiry_date</td> <td>The expiry date  of the customer's identity document. Example: 2025-01-31</td> </tr> <tr> <td>address</td> <td>Your customer's home or billing address mentioned on the identity document, utility bill or on a bank statement.</td> </tr> <tr> <td>first_name</td> <td>Customer’s first name on the identity document.</td> </tr> <tr> <td>middle_name</td> <td>Customer’s middle name on the identity document.</td> </tr> <tr> <td>last_name</td> <td>Customer’s last name on the identity document.</td> </tr> <tr> <td>dob</td> <td>Customer’s date of birth (YYYY-MM-DD). Example: 1980-01-31</td> </tr> <tr> <td>card_first_6_digits</td> <td>First 6 digits of the customer’s credit/debit card number if document type is debit/credit.</td> </tr> <tr> <td>card_last_4_digits</td> <td>Last 4 digits of the customer’s credit/debit card number if document type is debit/credit.</td> </tr> <tr> <td>background_checks</td> <td>Send 1 if you want us to perform background checks on your customer, 0 otherwise.</td> </tr> </tr> </table> |
| verification_data | Optional  | Required | If you want to perform an [offline verification](#offline-verification) without redirecting your customer to us, you can send us the identity docs using this parameter. The JSON encoded array of all the data required in the offline verification. The following keys are allowed to send in the request. In the below table keys are listed in left side column and right side column has detail of each key. <table><tr> <td>face_image</td> <td>The base64 string of your customer's selfie.  (Max size 4MB allowed)</td> </tr> <tr> <td>document_front_image</td> <td>The base64 string of the document mentioned  in “document_type” parameter (passport, driving_license, id_card). (Max size 4MB allowed)</td> </tr> <tr> <td>document_back_image</td> <td>The base64 string of the customer’s document back side image (if any). (Max size 4MB allowed)</td> </tr> <tr> <td>document_address_image</td> <td>The base64 string of the customer's utility bill or any document which must contain the residence address. If you want to verify the address then please send this image too. (Max size 4MB allowed)</td> </tr> <tr> <td>video</td> <td>The  base64  of the video is only required when the user wants to verify themselves through offline verification (by sending video). (Max size 8MB allowed)</td> </tr> </table> |
| signature | Required | Required | SHA256 hash of all the request parameters in sorted order. The details are in the signature calculation section. |


#  Get Request status
Once a verification request is completed, you may request to this end point to get the verification status. <br>

**Endpoint:**  	POST https://api.shuftipro.com/status <br>
**Format:**	    x-www-form-urlencoded

| Parameter | Required | Description |
| ------ | ------ | ------ |
| client_id | Yes | Client’s ID provided by Shufti Pro to you. (ID must be in alphanumeric format) |
| reference | Yes | Your unique request reference that you have sent at the time of request. (a valid request reference that is associated with  any request at the time it is made) |
| signature | Yes | Provide SHA256 hash of CONCATENATE(client_id, reference, secret_key) |

Find sample codes [here](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Get%20Request%20Status).

# Responses
The Shufti Pro API will send you two types of responses. First is the HTTP response sent against your request, and the second is the callback response, respectively. Both HTTP and callback responses will be in the JSON format and they will contain the following parameters:

| Parameter | Description |
| ------ | ------ |
| status_code | One of the status codes given [here](#status-codes). |
| message | The description of status code. If the status code is **SP2** then the message will be a redirect URL. |
| reference | Your unique request reference, which you provided us at the time of request, so that you can identify the response in relation to the request made. |
| signature | The **SHA256** hash of CONCATENATE(status_code, message, reference, secret_key). |


> **Note:** Callback response will be sent on the callback_url provided in the request **callback_url** parameter.


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
| SP16 | Missing required parameter -- ["parameter_name"] is required but either missing or empty. | Yes | Yes |
| SP17 | Invalid format -- ["parameter_name"] is  not  in the correct format. | Yes | Yes |
| SP18 | Invalid signature -- Invalid request signature. | Yes | Yes |
| SP19 | Invalid country code -- Invalid country code or country is not supported. | Yes | Yes |
| SP20 | Invalid Phone No -- Invalid phone number is provided. | Yes | Yes |
| SP21 | Invalid Method Name -- Given verification method is not supported. | Yes | Yes |
| SP22 | Invalid checksum value. | Yes | Yes |
| SP23 | Invalid DOB -- Date of birth is not valid. | Yes | Yes |
| SP24 | Blocked Client -- Your account is not active. | Yes | Yes |
| SP25 | Request Timeout -- Sends  in  callback when request timeouts. | Yes | Yes |
| SP26 | User has been landed on verification page. | Yes | Yes |
| SP27 | Request is already processed. | Yes | Yes |
| SP29 | Invalid size. The size limit for ["parameter_name"] is ["size in MBs"]. | Yes | Yes |
| SP30 | A particular verification service is not enabled. Please contact to the support. | Yes | Yes |
| SP32 | Invalid request reference. Request not found. | Yes | Yes |
| SP33 | Verification review pending. | Yes | Yes |
| SP34 | Language (provided in the request) is not supported. | Yes | Yes |
| SP35 | [parameter_name] not allowed with [method_name] verification method. | Yes | Yes |

# Signature Calculation
The request and response signature can be calculated as following: 
### *Request Signature*
1.  Sort all the request parameters (keys) in (ascending alphabetical order) 
and concatenate their values.
2.  Append the secret key at the end.
3. Calculate the SHA256 hash of string (made in above 2 steps).

### *Response Signature*
1.  Decode the JSON sent in the response body.
2.  Concatenate values of status_code, message, reference and secret key.
3.  Calculate the SHA256 hash of the string (made in above 2  steps).


# Sample Codes
Below are the sample codes in php, python & c# for the following verification methods: <br>
1.  [Online Identity verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Online%20Identity%20Verification)
2.  [Online Card Present verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Online%20Card%20Present%20Verification)
3.  [Offline Identity verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Offline%20Identity%20Verification)
4.  [Offline Card Present verification](https://github.com/shuftipro/integration-guide/tree/master/Sample%20codes/Offline%20Card%20Present%20Verification)

## Supported Languages
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


[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg?v=1)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realFace.jpg?v=1) 

[![](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg)](https://raw.githubusercontent.com/shuftipro/integration-guide/master/assets/realId.jpg) <br>




# Revision history 
| Date | Version | Description |
| ------ | ------ | ------ |
| March 14, 2018 | 1.0.1 | Added new endpoint for get request status. https://api.shuftipro.com/status |
| March 26, 2018 | 1.0.1 | Added lang parameter & supported languages list. |
| March 29, 2018 | 1.0.1 | Added C# sample codes. |
| April 10, 2018 | 1.0.1 | Added new supported languages. |




2016-18 © Shufti Pro Ltd.
