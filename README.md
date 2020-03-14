# WebCrawling-JobPortal-Monster.com-
This Mini Project features Scrapping data from monster.com and Storing in csv File of our own.
Modules Used = requests,csv,Selenium webdriver (Chrome) and BeautifulSoup.
Steps - 

Scenarios - There can be 2 Scenarios - 1.) Crawling A Static Webpage.   2.) Crawling a Dynamic Webpage
1.) Static Webpage - A static web page is a web page that is delivered to the user's web browser exactly as stored in form of html.So, in that case you 
 will be able to easily parse contents of a webpage using beautiful Soup.
2.) Dynamic Webpage - A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts. 
In server-side scripting, parameters determine how the assembly of every new web page proceeds, including the setting up of more client-side processing.
In That case , Use selenium Webdriver to entirely load the page and once everything is loaded , Then parse it using BeautifulSoup.

Guide for Scenario 1 -
1.) Make a http GET request to fetch source code of website to be crawled , It will return an Response Object . The source can then be extracted using .text() method on response object. 
2.) Once we get the source , We can parse it using BeautifulSoup and mentioning required parser(lxml,html5lib,etc). This will return an Soup Object in form of div elements.
3.) We can then programatically access values and  attributes once we get objectusing simple (.) operator.
4.) Using csv Module , Initialise Csv File and specify Operation to be preferred.Example - 
    csv_file= open('filename','w')
    Here , w specifies write Operation. If you want file in specific directory ,Mention entire path insteadof filename.
5.) Initialise csv writeUse using .writer() Method. Example -
    csv_file= open('filename','w')
    csv_exmple = csv.writer(csv_file)  
    Additionally,Use .writerow() Method to write headers in your csv file.
6.) Extract values from soup object using logic of your own in accordance with which data you specifically need.
7.) Use .write() Method to write values in csv file which you extracted from soup Object.
8.) Lastly, Close csv file. Example -
  csv_file.close()

Guide for Scenario 2 -

1.) Initialise Selenium webdriver . Example - 
  driver = webdriver.Chrome(executable_path = r"Path to chromdriver.exe")
  Note :If you have chromdriver.exe in same directory , directly mention 'chromdriver.exe'.
  
2.) Make request to fetch Source of webpage using .get() Method. Example - 
  driver.get("Url of webpage to be crawled")
  Note : Use Compatible Chrome Driver according to Your Google Chrome version in use.
3.)Fetch Source using -
    source = driver.execute_script("return document.documentElement.outerHTML")
    Note: source is not predefined keyword. Any variable name can beused here.
 4.) Repeat Steps 3 to 8 From Scenario 1.
 
 
 NOTE: IN THIS MINI-PROJECT SCENARIO 2 is implemented.
 
 
 Sachin Vyas
mailto : sachinvyas50@gmail.com 
 
   
 
 
   

