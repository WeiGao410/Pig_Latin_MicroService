# Pig_Latin_MicroService
Listen on port 80 and accept a string that contains at least one word, but potentially entire paragraphs. 
Convert the words in the string to Pig Latin and return the results in the HTTP message body.
Preserve all of the punctuation in the original string.
# Getting Started
Tools: python 2.7 environment and Chrome plugin Postman.
Just run the following command to get up server.
```bash
    'python server.py 8080'
```
The service will then be listening on port 8080(if port is already allocated, change to other port). If you visit the page http://localhost:8080/, you will see the welcome message.
# Using the Pig Latin translator
Using Postman to have the test.
##  Url
```
    http://localhost:8080/
```
## Method 
```
    POST
```
## Request Body
Fill in the Body with a sentence or paragraphs you like.
e.g.
```
    'If we didn't have stupid thoughts, we'd have no interesting thoughts at all.'
```
## Success Response

* **Status:** `200 OK`   
* **Time:** `16 ms`

### Response:
```
    Ifyay eway idn'tday avehay upidstay oughtsthay, e'dway avehay onay interestingyay oughtsthay atyay allyay.
```
# Running Tests
The test file is in the /test. You can run
```bash
    'python test.py'
```
If tests done successfully, you may see
```
Ran 8 tests in 0.001s

OK
```
 # Other Notes
 pigLatin.py can also run separately, just input a string and get the Pig Latin without the server support.
