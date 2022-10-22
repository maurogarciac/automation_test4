import pytest
from selenium import webdriver
from manager import Manager
from page_objects.home_page import HomePage

class Tests():

    
    @pytest.fixture(scope='module')
    def module_browser(self, request) -> webdriver:
        self.driver = Manager.get_driver()
        def fin():
            self.driver.quit()
        request.addfinalizer(fin())
        return self.driver


    # 1. Go to website
    #   website opens

    def test_1(self) -> None:
        homepage = HomePage(self.driver)
        homepage.go_to_page()
        assert True


    # 2. Go to Suggestion Class Element
    #   enter Me in the box
    #   iterate through value selected until it matches mexico
    #   it matches mexico
    #   (only use xpath)

    # 3. Go to Dropdown Element.
    #   select option 2
    #   select option 3
    #   option 3 is selected
    #   (only use xpath)

    # 4. Go to Switch Window Element.
    #   wait for page to load
    #   scroll down
    #   wait for popup to appear
    #   verify if the "30 day money back guarantee" text is visible
    #   (Review the SELF PACED ONLINE TRAINING, IN DEPTH MATERIAL,
    #   LIFETIME INSTRUCTOR SUPPORT and RESUME PREPARATION text to
    #   find the bugs and report them in the RTM)

    # 5. Go to Switch Tab Element
    #   Click the Open tab button
    #   Scroll to the "View all courses" button
    #   Take a screenshot that includes the button and name it like the TC
    #   Return to the first tab
    #   (Only use Xpath and Css)

    # 6. Go to Switch to Alert Element
    #   Input the string "Stori Card"
    #   Click the Alert button
    #   Print the text in the alert
    #   Click OK
    #   Make sure the text equals "Hello Stori Card, are you sure..."
    #   Click OK
    #   (Use Xpath and Css)

    # 7. Go to the Web Table Element.
    #   Print the amount of courses that are $25
    #   Print the name of every course that is $25
    #   (Use Css selector Child to Parent)

    # 8. Go to the Web Table Fixed Header Element.
    #   Print the name of all the engineers.
    #   (Use Xpath and Css child to parent)

    # 9. Go to the Iframe Web Element
    #   Hightlight some of the text in blue
    #   "His mentorship program..."
    #   (Use Xpath and print only the ODD indexes)

    # 10. Make an HTML Report with all test results
    #   Save it in a folder called Reports
    #   (make an XML report to)


