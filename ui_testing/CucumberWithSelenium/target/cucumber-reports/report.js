$(document).ready(function() {var formatter = new CucumberHTML.DOMFormatter($('.cucumber-report'));formatter.uri("Feature1Registration.feature");
formatter.feature({
  "line": 1,
  "name": "Registering a new user",
  "description": "",
  "id": "registering-a-new-user",
  "keyword": "Feature"
});
formatter.scenario({
  "line": 4,
  "name": "TestCase-101: Successful registration",
  "description": "",
  "id": "registering-a-new-user;testcase-101:-successful-registration",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 5,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 6,
  "name": "Enter registration credentials \"Jack\", \"Smith\", \"jack\", \"buu837@g.harvard.edu\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 7,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 8,
  "name": "Verify html element with class \"successmsg\" is \"We sent an email to buu837@g.harvard.edu.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 9,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 6748593458,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Jack",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "jack",
      "offset": 49
    },
    {
      "val": "buu837@g.harvard.edu",
      "offset": 57
    },
    {
      "val": "a1234567",
      "offset": 81
    },
    {
      "val": "a1234567",
      "offset": 96
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 594286209,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 2110929833,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "successmsg",
      "offset": 32
    },
    {
      "val": "We sent an email to buu837@g.harvard.edu.",
      "offset": 48
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 39680542,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 156912208,
  "status": "passed"
});
formatter.scenario({
  "line": 11,
  "name": "TestCase-102: Unsuccessful registration using already registered username",
  "description": "",
  "id": "registering-a-new-user;testcase-102:-unsuccessful-registration-using-already-registered-username",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 12,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 13,
  "name": "Enter registration credentials \"Jack\", \"Smith\", \"jack\", \"safakufuktepe@gmail.com\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 14,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 15,
  "name": "Verify html element with class \"errormsg\" is \"Username jack is already taken.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 16,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5332429208,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "Jack",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "jack",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 57
    },
    {
      "val": "a1234567",
      "offset": 84
    },
    {
      "val": "a1234567",
      "offset": 99
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 563982375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 847106750,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Username jack is already taken.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 35497791,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 122639500,
  "status": "passed"
});
formatter.scenario({
  "line": 18,
  "name": "TestCase-103: Unsuccessful registration using two different passwords",
  "description": "",
  "id": "registering-a-new-user;testcase-103:-unsuccessful-registration-using-two-different-passwords",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 19,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 20,
  "name": "Enter registration credentials \"John\", \"Smith\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"1234567a\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 21,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 22,
  "name": "Verify html element with class \"errormsg\" is \"Passwords must match.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 23,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5395180625,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 62
    },
    {
      "val": "1234567a",
      "offset": 89
    },
    {
      "val": "a1234567",
      "offset": 104
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 555043750,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 831586375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Passwords must match.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 36860292,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 155646542,
  "status": "passed"
});
formatter.scenario({
  "line": 25,
  "name": "TestCase-104: Unsuccessful registration using a blank username",
  "description": "",
  "id": "registering-a-new-user;testcase-104:-unsuccessful-registration-using-a-blank-username",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 26,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 27,
  "name": "Enter registration credentials \"John\", \"Smith\", \"\", \"safakufuktepe@gmail.com\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 28,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 29,
  "name": "Verify html element with class \"errormsg\" is \"Please provide a username.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 30,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5315234667,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 53
    },
    {
      "val": "a1234567",
      "offset": 80
    },
    {
      "val": "a1234567",
      "offset": 95
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 561350333,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 240858458,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Please provide a username.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 42735666,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 154622625,
  "status": "passed"
});
formatter.scenario({
  "line": 32,
  "name": "TestCase-105: Unsuccessful registration using a blank email",
  "description": "",
  "id": "registering-a-new-user;testcase-105:-unsuccessful-registration-using-a-blank-email",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 33,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 34,
  "name": "Enter registration credentials \"John\", \"Smith\", \"johnsmith\", \"\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 35,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 36,
  "name": "Verify html element with class \"errormsg\" is \"Please provide an email.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 37,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5384538375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 49
    },
    {
      "val": "",
      "offset": 62
    },
    {
      "val": "a1234567",
      "offset": 66
    },
    {
      "val": "a1234567",
      "offset": 81
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 557702583,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 255689208,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Please provide an email.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 39421625,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 145191375,
  "status": "passed"
});
formatter.scenario({
  "line": 39,
  "name": "TestCase-106: Unsuccessful registration using a blank first name",
  "description": "",
  "id": "registering-a-new-user;testcase-106:-unsuccessful-registration-using-a-blank-first-name",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 40,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 41,
  "name": "Enter registration credentials \"\", \"Smith\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 42,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 43,
  "name": "Verify html element with class \"errormsg\" is \"Please provide a first name.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 44,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 6388760583,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 36
    },
    {
      "val": "johnsmith",
      "offset": 45
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 58
    },
    {
      "val": "a1234567",
      "offset": 85
    },
    {
      "val": "a1234567",
      "offset": 100
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 545676084,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 272707541,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Please provide a first name.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 28869125,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 140780750,
  "status": "passed"
});
formatter.scenario({
  "line": 46,
  "name": "TestCase-107: Unsuccessful registration using a blank last name",
  "description": "",
  "id": "registering-a-new-user;testcase-107:-unsuccessful-registration-using-a-blank-last-name",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 47,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 48,
  "name": "Enter registration credentials \"John\", \"\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"a1234567\" and \"a1234567\"",
  "keyword": "When "
});
formatter.step({
  "line": 49,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 50,
  "name": "Verify html element with class \"errormsg\" is \"Please provide a last name.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 51,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5341937000,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 44
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 57
    },
    {
      "val": "a1234567",
      "offset": 84
    },
    {
      "val": "a1234567",
      "offset": 99
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 526498375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 261457375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Please provide a last name.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 32796666,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 145093833,
  "status": "passed"
});
formatter.scenario({
  "line": 53,
  "name": "TestCase-108: Unsuccessful registration using a blank password",
  "description": "",
  "id": "registering-a-new-user;testcase-108:-unsuccessful-registration-using-a-blank-password",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 54,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 55,
  "name": "Enter registration credentials \"John\", \"Smith\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"\" and \"\"",
  "keyword": "When "
});
formatter.step({
  "line": 56,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 57,
  "name": "Verify html element with class \"errormsg\" is \"Your password must be at least 8 characters long.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 58,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5302294000,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 62
    },
    {
      "val": "",
      "offset": 89
    },
    {
      "val": "",
      "offset": 96
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 546717958,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 887477917,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Your password must be at least 8 characters long.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 39279417,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 150083667,
  "status": "passed"
});
formatter.scenario({
  "line": 60,
  "name": "TestCase-109: Unsuccessful registration using a short password",
  "description": "",
  "id": "registering-a-new-user;testcase-109:-unsuccessful-registration-using-a-short-password",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 61,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 62,
  "name": "Enter registration credentials \"John\", \"Smith\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"a1234\" and \"a1234\"",
  "keyword": "When "
});
formatter.step({
  "line": 63,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 64,
  "name": "Verify html element with class \"errormsg\" is \"Your password must be at least 8 characters long.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 65,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5338283708,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 62
    },
    {
      "val": "a1234",
      "offset": 89
    },
    {
      "val": "a1234",
      "offset": 101
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 545909792,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 806863250,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Your password must be at least 8 characters long.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 30853209,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 155670583,
  "status": "passed"
});
formatter.scenario({
  "line": 67,
  "name": "TestCase-110: Unsuccessful registration using a password that is entirely numeric",
  "description": "",
  "id": "registering-a-new-user;testcase-110:-unsuccessful-registration-using-a-password-that-is-entirely-numeric",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 68,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 69,
  "name": "Enter registration credentials \"John\", \"Smith\", \"johnsmith\", \"safakufuktepe@gmail.com\", \"12345678\" and \"12345678\"",
  "keyword": "When "
});
formatter.step({
  "line": 70,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 71,
  "name": "Verify html element with class \"errormsg\" is \"Your password cannot be entirely numeric.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 72,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5387222125,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "John",
      "offset": 32
    },
    {
      "val": "Smith",
      "offset": 40
    },
    {
      "val": "johnsmith",
      "offset": 49
    },
    {
      "val": "safakufuktepe@gmail.com",
      "offset": 62
    },
    {
      "val": "12345678",
      "offset": 89
    },
    {
      "val": "12345678",
      "offset": 104
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 528384292,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 822300333,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Your password cannot be entirely numeric.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 31166958,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 152915375,
  "status": "passed"
});
formatter.scenario({
  "line": 74,
  "name": "TestCase-111: Unsuccessful registration using a blank form",
  "description": "",
  "id": "registering-a-new-user;testcase-111:-unsuccessful-registration-using-a-blank-form",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 75,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/register\"",
  "keyword": "Given "
});
formatter.step({
  "line": 76,
  "name": "Enter registration credentials \"\", \"\", \"\", \"\", \"\" and \"\"",
  "keyword": "When "
});
formatter.step({
  "line": 77,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 78,
  "name": "Verify html element with class \"errormsg\" is \"Please provide a username.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 79,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/register",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5312507417,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "",
      "offset": 32
    },
    {
      "val": "",
      "offset": 36
    },
    {
      "val": "",
      "offset": 40
    },
    {
      "val": "",
      "offset": 44
    },
    {
      "val": "",
      "offset": 48
    },
    {
      "val": "",
      "offset": 55
    }
  ],
  "location": "Steps.enter_registration_credentials(String,String,String,String,String,String)"
});
formatter.result({
  "duration": 417205625,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 217237167,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Please provide a username.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 29709291,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 147640458,
  "status": "passed"
});
formatter.uri("Feature2Login.feature");
formatter.feature({
  "line": 1,
  "name": "Logging into the user\u0027s account",
  "description": "",
  "id": "logging-into-the-user\u0027s-account",
  "keyword": "Feature"
});
formatter.scenario({
  "line": 4,
  "name": "TestCase-201: Successful login",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-201:-successful-login",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 5,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 6,
  "name": "Enter login credentials \"burak\", \"1234\"",
  "keyword": "When "
});
formatter.step({
  "line": 7,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 8,
  "name": "Verify html element with id \"profilelink\" is \"Profile\"",
  "keyword": "Then "
});
formatter.step({
  "line": 9,
  "name": "Logout",
  "keyword": "Then "
});
formatter.step({
  "line": 10,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5328027292,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "burak",
      "offset": 25
    },
    {
      "val": "1234",
      "offset": 34
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 337051417,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 2744125125,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "profilelink",
      "offset": 29
    },
    {
      "val": "Profile",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_id(String,String)"
});
formatter.result({
  "duration": 53892666,
  "status": "passed"
});
formatter.match({
  "location": "Steps.logout()"
});
formatter.result({
  "duration": 1635779667,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 133201041,
  "status": "passed"
});
formatter.scenario({
  "line": 12,
  "name": "TestCase-202: Unsuccessful login using an invalid username",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-202:-unsuccessful-login-using-an-invalid-username",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 13,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 14,
  "name": "Enter login credentials \"aaa\", \"1234\"",
  "keyword": "When "
});
formatter.step({
  "line": 15,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 16,
  "name": "Verify html element with class \"errormsg\" is \"Invalid username and/or password.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 17,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5314157583,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "aaa",
      "offset": 25
    },
    {
      "val": "1234",
      "offset": 32
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 329089792,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 940492916,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Invalid username and/or password.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 36806000,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 101593208,
  "status": "passed"
});
formatter.scenario({
  "line": 19,
  "name": "TestCase-203: Unsuccessful login using an invalid password",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-203:-unsuccessful-login-using-an-invalid-password",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 20,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 21,
  "name": "Enter login credentials \"burak\", \"12\"",
  "keyword": "When "
});
formatter.step({
  "line": 22,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 23,
  "name": "Verify html element with class \"errormsg\" is \"Invalid username and/or password.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 24,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5261812209,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "burak",
      "offset": 25
    },
    {
      "val": "12",
      "offset": 34
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 363454917,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 1007664875,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Invalid username and/or password.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 35718208,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 104833542,
  "status": "passed"
});
formatter.scenario({
  "line": 26,
  "name": "TestCase-204: Unsuccessful login using a blank username",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-204:-unsuccessful-login-using-a-blank-username",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 27,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 28,
  "name": "Enter login credentials \"\", \"12\"",
  "keyword": "When "
});
formatter.step({
  "line": 29,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 30,
  "name": "Verify html element with class \"errormsg\" is \"Invalid username and/or password.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 31,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5301695167,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "",
      "offset": 25
    },
    {
      "val": "12",
      "offset": 29
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 345207125,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 895849750,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Invalid username and/or password.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 35655375,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 153665042,
  "status": "passed"
});
formatter.scenario({
  "line": 33,
  "name": "TestCase-205: Unsuccessful login using a blank password",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-205:-unsuccessful-login-using-a-blank-password",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 34,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 35,
  "name": "Enter login credentials \"burak\", \"\"",
  "keyword": "When "
});
formatter.step({
  "line": 36,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 37,
  "name": "Verify html element with class \"errormsg\" is \"Invalid username and/or password.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 38,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5354391125,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "burak",
      "offset": 25
    },
    {
      "val": "",
      "offset": 34
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 358370208,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 887408667,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Invalid username and/or password.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 31808667,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 138923791,
  "status": "passed"
});
formatter.scenario({
  "line": 40,
  "name": "TestCase-206: Unsuccessful login using a blank username and password",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-206:-unsuccessful-login-using-a-blank-username-and-password",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 41,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/login\"",
  "keyword": "Given "
});
formatter.step({
  "line": 42,
  "name": "Enter login credentials \"\", \"\"",
  "keyword": "When "
});
formatter.step({
  "line": 43,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 44,
  "name": "Verify html element with class \"errormsg\" is \"Invalid username and/or password.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 45,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/login",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5462010459,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "",
      "offset": 25
    },
    {
      "val": "",
      "offset": 29
    }
  ],
  "location": "Steps.enter_login_credentials(String,String)"
});
formatter.result({
  "duration": 315722708,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 798080375,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "errormsg",
      "offset": 32
    },
    {
      "val": "Invalid username and/or password.",
      "offset": 46
    }
  ],
  "location": "Steps.verify_html_element_with_class(String,String)"
});
formatter.result({
  "duration": 40243459,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 150385833,
  "status": "passed"
});
formatter.scenario({
  "line": 47,
  "name": "TestCase-207: Successful password reset",
  "description": "",
  "id": "logging-into-the-user\u0027s-account;testcase-207:-successful-password-reset",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 48,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/password_reset\"",
  "keyword": "Given "
});
formatter.step({
  "line": 49,
  "name": "Enter email for password reset \"bufuktepe@gmail.com\"",
  "keyword": "When "
});
formatter.step({
  "line": 50,
  "name": "Click button with class name \"btn\"",
  "keyword": "Then "
});
formatter.step({
  "line": 51,
  "name": "Verify html element with id \"resetpasswordconfirm\" is \"Reset password email sent.\"",
  "keyword": "Then "
});
formatter.step({
  "line": 52,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/password_reset",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 5253773625,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "bufuktepe@gmail.com",
      "offset": 32
    }
  ],
  "location": "Steps.enter_login_credentials(String)"
});
formatter.result({
  "duration": 325176333,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "btn",
      "offset": 30
    }
  ],
  "location": "Steps.click_button_with_class_name(String)"
});
formatter.result({
  "duration": 847616916,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "resetpasswordconfirm",
      "offset": 29
    },
    {
      "val": "Reset password email sent.",
      "offset": 55
    }
  ],
  "location": "Steps.verify_html_element_with_id(String,String)"
});
formatter.result({
  "duration": 54350500,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 156481458,
  "status": "passed"
});
formatter.uri("Feature3Search.feature");
formatter.feature({
  "line": 1,
  "name": "Conducting Search",
  "description": "",
  "id": "conducting-search",
  "keyword": "Feature"
});
formatter.scenario({
  "line": 4,
  "name": "TestCase-301: Successful search - criteria: library layout",
  "description": "",
  "id": "conducting-search;testcase-301:-successful-search---criteria:-library-layout",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 5,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22librarylayout%22:%20[%22PAIRED%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20false}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 6,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 7,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22librarylayout%22:%20[%22PAIRED%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20false}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 8267060584,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 317687083,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 196545667,
  "status": "passed"
});
formatter.scenario({
  "line": 9,
  "name": "TestCase-302: Successful search - criteria: sra study",
  "description": "",
  "id": "conducting-search;testcase-302:-successful-search---criteria:-sra-study",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 10,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22sra_study%22:%20[%22SRP002462%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 11,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 12,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22sra_study%22:%20[%22SRP002462%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9297318583,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 221368084,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 160532458,
  "status": "passed"
});
formatter.scenario({
  "line": 14,
  "name": "TestCase-303: Successful search - criteria: center name",
  "description": "",
  "id": "conducting-search;testcase-303:-successful-search---criteria:-center-name",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 15,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22center_name%22:%20[%22HARVARD%20MEDICAL%20SCHOOL%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 16,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 17,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22center_name%22:%20[%22HARVARD%20MEDICAL%20SCHOOL%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 8940168125,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 322345916,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 148777875,
  "status": "passed"
});
formatter.scenario({
  "line": 19,
  "name": "TestCase-304: Successful search - criteria: experiment ID",
  "description": "",
  "id": "conducting-search;testcase-304:-successful-search---criteria:-experiment-id",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 20,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22experiment%22:%20[%22ERX084377%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 21,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 22,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22experiment%22:%20[%22ERX084377%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 8855255792,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 98144750,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 140760250,
  "status": "passed"
});
formatter.scenario({
  "line": 24,
  "name": "TestCase-305: Successful search - criteria: sample ACC",
  "description": "",
  "id": "conducting-search;testcase-305:-successful-search---criteria:-sample-acc",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 25,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22sample_acc%22:%20[%22SRS1466819%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 26,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 27,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22sample_acc%22:%20[%22SRS1466819%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9497466250,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 114811083,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 141983833,
  "status": "passed"
});
formatter.scenario({
  "line": 29,
  "name": "TestCase-306: Successful search - criteria: biosample",
  "description": "",
  "id": "conducting-search;testcase-306:-successful-search---criteria:-biosample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 30,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22biosample%22:%20[%22SAMEA3543292%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 31,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 32,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22biosample%22:%20[%22SAMEA3543292%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9076428167,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 112017541,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 132690791,
  "status": "passed"
});
formatter.scenario({
  "line": 34,
  "name": "TestCase-307: Successful search - criteria: organism",
  "description": "",
  "id": "conducting-search;testcase-307:-successful-search---criteria:-organism",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 35,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22organism%22:%20[%22gut%20metagenome%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 36,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 37,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22organism%22:%20[%22gut%20metagenome%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9087728708,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 325975292,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 132003042,
  "status": "passed"
});
formatter.scenario({
  "line": 39,
  "name": "TestCase-308: Successful search - criteria: bioproject",
  "description": "",
  "id": "conducting-search;testcase-308:-successful-search---criteria:-bioproject",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 40,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22bioproject%22:%20[%22PRJEB10006%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 41,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 42,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22bioproject%22:%20[%22PRJEB10006%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9830990417,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 307043250,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 174760250,
  "status": "passed"
});
formatter.scenario({
  "line": 44,
  "name": "TestCase-309: Successful search - criteria: country",
  "description": "",
  "id": "conducting-search;testcase-309:-successful-search---criteria:-country",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 45,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22geo_loc_name_country_calc%22:%20[%22Japan%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 46,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 47,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22geo_loc_name_country_calc%22:%20[%22Japan%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9547637250,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 375466791,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 292585250,
  "status": "passed"
});
formatter.scenario({
  "line": 49,
  "name": "TestCase-310: Successful search - criteria: continent",
  "description": "",
  "id": "conducting-search;testcase-310:-successful-search---criteria:-continent",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 50,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22geo_loc_name_country_continent_calc%22:%20[%22Africa%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 51,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 52,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22geo_loc_name_country_continent_calc%22:%20[%22Africa%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9398092500,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 337197542,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 153556667,
  "status": "passed"
});
formatter.scenario({
  "line": 54,
  "name": "TestCase-311: Successful search - criteria: breed sample",
  "description": "",
  "id": "conducting-search;testcase-311:-successful-search---criteria:-breed-sample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 55,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22breed_sam%22:%20[%22Human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 56,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 57,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22breed_sam%22:%20[%22Human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9723999083,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 319006959,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 244179625,
  "status": "passed"
});
formatter.scenario({
  "line": 59,
  "name": "TestCase-312: Successful search - criteria: cultivar sample",
  "description": "",
  "id": "conducting-search;testcase-312:-successful-search---criteria:-cultivar-sample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 60,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22cultivar_sam%22:%20[%2240BL24hr%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 61,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 62,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22cultivar_sam%22:%20[%2240BL24hr%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9182314917,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 121878458,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 134092917,
  "status": "passed"
});
formatter.scenario({
  "line": 64,
  "name": "TestCase-313: Successful search - criteria: ecotype sample",
  "description": "",
  "id": "conducting-search;testcase-313:-successful-search---criteria:-ecotype-sample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 65,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22ecotype_sam%22:%20[%22Asian%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 66,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 67,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22ecotype_sam%22:%20[%22Asian%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9215464208,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 373233250,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 128245875,
  "status": "passed"
});
formatter.scenario({
  "line": 69,
  "name": "TestCase-314: Successful search - criteria: isolate sample",
  "description": "",
  "id": "conducting-search;testcase-314:-successful-search---criteria:-isolate-sample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 70,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22isolate_sam%22:%20[%22human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 71,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 72,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22isolate_sam%22:%20[%22human%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9627753417,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 277894458,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 136338875,
  "status": "passed"
});
formatter.scenario({
  "line": 74,
  "name": "TestCase-315: Successful search - criteria: library selection",
  "description": "",
  "id": "conducting-search;testcase-315:-successful-search---criteria:-library-selection",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 75,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22libraryselection%22:%20[%22PCR%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 76,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 77,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22libraryselection%22:%20[%22PCR%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 8553904541,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 274611500,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 198915625,
  "status": "passed"
});
formatter.scenario({
  "line": 79,
  "name": "TestCase-316: Successful search - criteria: strain sample",
  "description": "",
  "id": "conducting-search;testcase-316:-successful-search---criteria:-strain-sample",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 80,
  "name": "Open Chrome and launch the application with url \"http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22strain_sam%22:%20[%220821200151%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}\"",
  "keyword": "Given "
});
formatter.step({
  "line": 81,
  "name": "Verify html element with class exists \"table-generic-td\"",
  "keyword": "Then "
});
formatter.step({
  "line": 82,
  "name": "Close Browser",
  "keyword": "Then "
});
formatter.match({
  "arguments": [
    {
      "val": "http://127.0.0.1:8000/filtered_table/1/acc/asc/?search_criteria\u003d{%22strain_sam%22:%20[%220821200151%22],%20%22only_processed_studies%22:%20false,%20%22include_sra_studies%22:%20true,%20%22include_private_studies%22:%20true}",
      "offset": 49
    }
  ],
  "location": "Steps.open_Chrome_and_launch_the_application(String)"
});
formatter.result({
  "duration": 9123118875,
  "status": "passed"
});
formatter.match({
  "arguments": [
    {
      "val": "table-generic-td",
      "offset": 39
    }
  ],
  "location": "Steps.verify_html_element_with_class_exists(String)"
});
formatter.result({
  "duration": 110067791,
  "status": "passed"
});
formatter.match({
  "location": "Steps.close_browser()"
});
formatter.result({
  "duration": 130944000,
  "status": "passed"
});
});