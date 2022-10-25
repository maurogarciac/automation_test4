Feature: Fight or flight
  In order to ,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  Scenario: Access smoke test
    Given browser opens
     When url is searched for
     Then page loads

  Scenario: Suggestion
    Given home page is open
     When enter Me in the suggestion input box
     Then a suggestion for Mexico can be selected

  Scenario: Dropdown
    Given home page is open
     When option 2 is selected in the Dropdown class
     Then option 3 can be selected
     And selection is updated to option 3

  Scenario: Switch Windows
    Given home page is open
     When the switch window button is clicked
     Then a text that says <guarantee> is visible

    |guarantee|
    |"30 day money back guarantee"|

  Scenario: Switch Tabs
    Given home page is open
     When the switch tab button is clicked
     Then the view all courses button is visible

  Scenario: Switch to Alert
    Given home page is open
     When the switch to alert input box is visible
     Then <string> is input into the box
     Then the alert button is clicked
     And the OK button is clicked
     Then the message equals <message>
     Then the OK button is clicked

     |string|message|
     |"Stori Card"|Hello Stori Card, are you sure...|
     
  Scenario: Web Table
    Given home page is open
     When the table element is found
     Then the total of the courses sold for $25 is printed
     And the list of courses sold for $25 is printed

  Scenario: Web Table FE
    Given home page is open
     When the table fixed header is found
     Then the name of all the engineers is printed

  Scenario: IFrame
    Given home page is open
     When the switch tab button is clicked
     Then the view all courses button is visible

    # 8. Go to the Web Table Fixed Header Element.
    #   Print the name of all the engineers.
    #   (Use Xpath and Css child to parent)

    # 9. Go to the Iframe Web Element
    #   Hightlight some of the text in blue
    #   "His mentorship program..."
    #   (Use Xpath and print only the ODD indexes)
