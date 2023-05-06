Feature: Registering a new user


	Scenario: TestCase-101: Successful registration 
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"			
		When Enter registration credentials "Jack", "Smith", "jack", "buu837@g.harvard.edu", "a1234567" and "a1234567"			
		Then Click button with class name "btn"
		Then Verify html element with class "successmsg" is "We sent an email to buu837@g.harvard.edu."
		Then Close Browser
		
	Scenario: TestCase-102: Unsuccessful registration using already registered username
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "Jack", "Smith", "jack", "safakufuktepe@gmail.com", "a1234567" and "a1234567"				
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Username jack is already taken."
		Then Close Browser

	Scenario: TestCase-103: Unsuccessful registration using two different passwords
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "johnsmith", "safakufuktepe@gmail.com", "1234567a" and "a1234567"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Passwords must match."
		Then Close Browser
		
	Scenario: TestCase-104: Unsuccessful registration using a blank username
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "", "safakufuktepe@gmail.com", "a1234567" and "a1234567"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Please provide a username."
		Then Close Browser
	
	Scenario: TestCase-105: Unsuccessful registration using a blank email
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "johnsmith", "", "a1234567" and "a1234567"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Please provide an email."
		Then Close Browser
		
	Scenario: TestCase-106: Unsuccessful registration using a blank first name
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "", "Smith", "johnsmith", "safakufuktepe@gmail.com", "a1234567" and "a1234567"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Please provide a first name."
		Then Close Browser
		
	Scenario: TestCase-107: Unsuccessful registration using a blank last name
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "", "johnsmith", "safakufuktepe@gmail.com", "a1234567" and "a1234567"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Please provide a last name."
		Then Close Browser
		
	Scenario: TestCase-108: Unsuccessful registration using a blank password
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "johnsmith", "safakufuktepe@gmail.com", "" and ""		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Your password must be at least 8 characters long."
		Then Close Browser
		
	Scenario: TestCase-109: Unsuccessful registration using a short password
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "johnsmith", "safakufuktepe@gmail.com", "a1234" and "a1234"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Your password must be at least 8 characters long."
		Then Close Browser
		
	Scenario: TestCase-110: Unsuccessful registration using a password that is entirely numeric
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "John", "Smith", "johnsmith", "safakufuktepe@gmail.com", "12345678" and "12345678"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Your password cannot be entirely numeric."
		Then Close Browser
		
	Scenario: TestCase-111: Unsuccessful registration using a blank form
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/register"		
		When Enter registration credentials "", "", "", "", "" and ""		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Please provide a username."
		Then Close Browser