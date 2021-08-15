## A Take Home Assessment 
![pic](assessment.jpg)  
# Basic Tests for QA Engineer Role at unbugQA

## Tools and Framework used
* Framework: [Behave](https://behave.readthedocs.io/en/stable/)
* Supporting Language: Python 3.9.0
* Test Site: [Seleniumeasy](https://www.seleniumeasy.com/test/) 
* Supporting Libraries:
    * [Selenium](https://www.selenium.dev/)
    * [python-dotenv](https://pypi.org/project/python-dotenv/)
    * [brew](https://brew.sh/)
    * [Webdriver: Chrome](https://chromedriver.chromium.org/)
    * Framework version: Check requirements.txt file
    * [IDE: Pycharm (Community Edition)](https://www.jetbrains.com/pycharm/)
    * OS: macOS (Catalina 11.2.3)

## Setup
### Recommendation
I will recommend that a virtual environment be set up
within the project to run locally. You can use pyenv or
virtualenv to set up. This will allow the dependencies and
libraries installed to be inside the project alone.

Once the virtual environment has been setup and activated,
proceed to install the libraries in the `requirements.txt` file with the
command `pip install -r requirements.txt`.

## Installation and usage. (Starting from Scratch)
Installation and usage can be done via the terminal or used through the Pycharm IDE or VsCode.
### Using the Terminal
* Open terminal
* Install python by running _**"brew install python3"**_ (for Mac)
* Install python from python website (for Windows)
* Navigate into the project folder then create the virtual environment
* Activate the virtual environment using `source <virtual env name/bin/activate` (for Mac).
* Activate the virtual environment using `<virtual env name\Scripts\activate` (for Windows).
* Install behave and selenium by running `pip install -r requirements.txt`
* Install chromedriver by running `brew cask install chromedriver` (for Mac) and add to Path
* Install chromedriver via web (For Windows) and add to Path
### Docker

If you have docker installed, you can execute the script in a headless mode by running 'bash headless.sh' from the root folder of the project.
This will build the docker file and execute the scripts.

### Non-headless mode
Install python and navigate into the root folder of the project. After that, install and setup the virtual environment and create the virtual environment. Activate the virtual environment as described above then install all requirements from the requirements.txt then run `bash non-headless.sh`

### Scenarios Automated
* Input Forms
  * A user should be able to click a single checkbox
  * A user should be able to click to check all checkboxes
  * A user should be able to click to uncheck all checkboxes  
* Alerts & Modals
  * A user should see alert box and click ok
  * A user should be able to confirm an alert box
  * A user should be able to cancel an alert box
  * A user should be able to confirm an alert box with a text  
* List Box
  * A user should be able to add one name
  * A user should be able to add more than one name
  * A user should be able to add all names
  * A user should be able to remove all names  