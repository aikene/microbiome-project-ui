package StepDefinition;		

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.Duration;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import cucumber.api.java.en.Given;		
import cucumber.api.java.en.Then;		
import cucumber.api.java.en.When;

public class Steps {				

    WebDriver driver;			
    		
    @Given("^Open Chrome and launch the application with url \"([^\"]*)\"$")					
    public void open_Chrome_and_launch_the_application(String url) throws Throwable							
    {		
       System.setProperty("webdriver.gecko.driver", "E://Selenium//Selenium_Jars//geckodriver.exe");		
       ChromeOptions options = new ChromeOptions();
       options.addArguments("--remote-allow-origins=*");
       
       
       driver = new ChromeDriver(options);					
       driver.manage().window().maximize();			
       driver.get(url);
    }		

    @When("^Enter registration credentials \"([^\"]*)\", \"([^\"]*)\", \"([^\"]*)\", \"([^\"]*)\", \"([^\"]*)\" and \"([^\"]*)\"$")					
    public void enter_registration_credentials(String firstName, String lastName, String username, String email, String password, String confirmPassword) throws Throwable 							
    {		
       driver.findElement(By.name("first-name")).sendKeys(firstName);
       driver.findElement(By.name("last-name")).sendKeys(lastName);	
       driver.findElement(By.name("username")).sendKeys(username);							
       driver.findElement(By.name("email")).sendKeys(email);	
       driver.findElement(By.name("password")).sendKeys(password);
       driver.findElement(By.name("confirmation")).sendKeys(confirmPassword);
    }		

    @Then("^Click button with class name \"([^\"]*)\"$")					
    public void click_button_with_class_name(String clsName) throws Throwable 							
    {		
       driver.findElement(By.className(clsName)).click();		
    }	
    
    @Then("^Click button with id \"([^\"]*)\"$")					
    public void click_button_with_id(String identifier) throws Throwable 							
    {		
       driver.findElement(By.id(identifier)).click();		
    }	
    
    @Then("^Wait and click button with id \"([^\"]*)\"$")					
    public void wait_andclick_button_with_id(String identifier) throws Throwable 							
    {		
    	driver.navigate().refresh();
    	
    	WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(3));
    	
    	WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id(identifier)));
    	element.click();

//		JavascriptExecutor js = (JavascriptExecutor) driver;
//		js.executeScript("window.scrollTo(0, document.body.scrollHeight)");
//
//
//    	WebElement myElement = new WebDriverWait(driver, Duration.ofSeconds(3)).until(ExpectedConditions.visibilityOf(element));
//
//    	Actions actions = new Actions(driver);
//    	actions.moveToElement(myElement).click().build().perform();

//    	element.click();
    	
//       driver.findElement(By.id(identifier)).click();		
    }
    
    @Then("^Verify html element with name \"([^\"]*)\" is \"([^\"]*)\"$")					
    public void verify_html_element_with_name(String htmlElm, String expected) throws Throwable 							
    {		
       String actual=driver.findElement(By.name(htmlElm)).getText();
       assert(expected.equals(actual));
    }	
    
    @Then("^Verify html element with id \"([^\"]*)\" is \"([^\"]*)\"$")					
    public void verify_html_element_with_id(String htmlElm, String expected) throws Throwable 							
    {		
       String actual=driver.findElement(By.id(htmlElm)).getText();
       assert(expected.equals(actual));
    }	
    
    @Then("^Verify html element with class \"([^\"]*)\" is \"([^\"]*)\"$")					
    public void verify_html_element_with_class(String htmlElm, String expected) throws Throwable 							
    {		
       String actual=driver.findElement(By.className(htmlElm)).getText();
       assert(expected.equals(actual));
    }	
    
    @Then("^Verify html element with class exists \"([^\"]*)\"$")				
    public void verify_html_element_with_class_exists(String htmlElm) throws Throwable 							
    {		
       List<WebElement> elements = driver.findElements(By.className(htmlElm));
       assert(elements.size() > 0);
    }
    
    @Then("^Verify html element with href \"([^\"]*)\" is \"([^\"]*)\"$")					
    public void verify_html_element_with_href(String urlStr, String expected) throws Throwable 							
    {		
       String actual=driver.findElement(By.xpath("//a[@href=\"" + urlStr + "\"]")).getText();
       assert(expected.equals(actual));
    }
    
    @When("^Enter login credentials \"([^\"]*)\", \"([^\"]*)\"$")					
    public void enter_login_credentials(String username, String password) throws Throwable 							
    {		
       driver.findElement(By.name("username")).sendKeys(username);								
       driver.findElement(By.name("password")).sendKeys(password);
    }
    
    @When("^Enter email for password reset \"([^\"]*)\"$")					
    public void enter_login_credentials(String email) throws Throwable 							
    {		
       driver.findElement(By.name("email")).sendKeys(email);								
    }
    
    @Then("^Logout$")					
    public void logout() throws Throwable 							
    {		
       driver.findElement(By.id("logout")).click();	
    }
    
    @Then("^Close Browser$")					
    public void close_browser() throws Throwable 							
    {		
       driver.close();	
    }
    
    @When("^Select dropdown item \"([^\"]*)\", \"([^\"]*)\"$")	
    public void select_dropdown_item(String htmlElm, String itemName) throws Throwable 							
    {		
    	WebElement selectElement = driver.findElement(By.name(htmlElm));
        Select select = new Select(selectElement);
        
        select.selectByVisibleText(itemName);
    }	

}