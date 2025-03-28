"""


// locators - find elements on webpage

-- locators ( can directly find in HTML file )
- ID
- NAME
- LINKTEXT
- PARTIALLINKTEXT
- CLASSNAME
-TAGNAME

-- HTML structure
- <input name="usernsame" id="uniqueIdentifier" type="text">
input = element / tag name
name , id, type = Attribute
value = username, text, uniqueidentifier

// relative path
//abslute path

// tag[@attribute='value']
// *[@attribute='value'] - works on any tag name with that attribute

// to view console > view > developer > developer tools

// using contains
$x('ul[contains(@id, "id-name" )]'

// find by text
$x('//a[text()="Lost your password"]')


// find element

id and name
_driver.FindElement(By.Id("userName"));
_driver.FindElement(By.Name("webDriverCheatSheet"));


linktext and partial linktext
--- use for links ( a elements href attributes  )
- finds elements by the link text

Example : <a href="https://example.com/about" id="about-link">About Us</a>
Full link : driver.find_element(By.LINK_TEXT, "About Us").click()
partial link : driver.FindElement(By.PartialLinkText("About"));


tag name & class name
// finds first occurance
_driver.FindElement(By.ClassName("panel other"));
_driver.FindElement(By.TagName("a"));

// finds multiple
_driver.FindElements(By.ClassName("panel other"));
_driver.FindElements(By.TagName("a"));


_driver.FindElement(By.CssSelector("#userName"));
_driver.FindElement(By.Name("webDriverCheatSheet"));
_driver.FindElement(By.XPath("//*[@id='panel']/div/h1"));


-- customized locators :
** x path if can't find ID or CSS Selector

- CSS SELECTORS
 - to use in browser console : $$()
 EX :
 $$("#idname")


- tag and ID

tagname#IDname  - input#email
or
#IDname

EX : driver.find_element(By.CSS_SELECTOR, "input#email")
    driver.find_element(By.CSS_SELECTOR, "#email")

    or driver.findElement(By.ID, "id name")


- tag and class

tagname.CLASSValue

EX : driver.find_element(By.CSS_SELECTOR, "input.inputtext")
driver.find_element(By.CSS_SELECTOR, ".inputtext")



- tag and attribute

tagName[attribute=value]

 EX : driver.find_element(By.CSS_SELECTOR, input[data-testid=email]")

- tag, class and attribute


Go from  upper element to child element
#upperelement input.classname.ofchildelement
- XPath






CSS cs XPATH
- css is faster , does not locate by text



Behavior Driven Development ( BDD )

- describes the behavior and expected outcome of a software system befor ebuilding it

2 steps :
- define the desired behavior of the software
- build the software


scenario -  test case name
given - preconditions
when - actions of test case
then - verificaiton
and - duplicates the word above



all files with test cases have feature in name "product_search.feature"




"""



