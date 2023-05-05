Feature: Logging into the user's account

		
	Scenario: TestCase-201: Successful login
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "burak", "1234"		
		Then Click button with class name "btn"
		Then Verify html element with id "profilelink" is "Profile"
		Then Logout
		Then Close Browser
		
	Scenario: TestCase-202: Unsuccessful login using an invalid username
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "aaa", "1234"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Invalid username and/or password."
		Then Close Browser
		
	Scenario: TestCase-203: Unsuccessful login using an invalid password
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "burak", "12"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Invalid username and/or password."
		Then Close Browser
		
	Scenario: TestCase-204: Unsuccessful login using a blank username
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "", "12"		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Invalid username and/or password."
		Then Close Browser
		
	Scenario: TestCase-205: Unsuccessful login using a blank password
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "burak", ""		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Invalid username and/or password."
		Then Close Browser
		
	Scenario: TestCase-206: Unsuccessful login using a blank username and password
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/login"				
		When Enter login credentials "", ""		
		Then Click button with class name "btn"
		Then Verify html element with class "errormsg" is "Invalid username and/or password."
		Then Close Browser
		
	Scenario: TestCase-207: Successful password reset
		Given Open Chrome and launch the application with url "http://127.0.0.1:8000/password_reset"				
		When Enter email for password reset "bufuktepe@gmail.com"		
		Then Click button with class name "btn"
		Then Verify html element with id "resetpasswordconfirm" is "Reset password email sent."
		Then Close Browser
		