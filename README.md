How To
==============
## Dependencies
* Tested on Python 3.7, Appium 1.10.0
* pip install -r requirements.txt

## Run Syntax
* To ATR (All Tests Run): 
    * To run for QA server: fire the *server-master.sh
    * To run for Dev server: fire the *server-develop.sh
* You can use -m 'tier1' or -k 'your_keyword' or combine  -m and -k to select the test cases to run

## How to configure run environment
* Setup system env for APPIUM_URL, APP_PATH, PLATFORM_VERSION, OLD_CART_UI, IS_PRINTER_CONFIGURED and xxx_QA
    * APPIUM_URL specifies the appium URL, by default, 'http://localhost:4723/wd/hub'
    * APP_PATH specifies the absolute path to your apk, say, '/Users/huanglh/Downloads/xxx.apk'
    * PLATFORM_VERSION specifies your Android OS version, say, 7.1.1. The code is certified with Sunmi 7.1.1 and Sunmi 6.0.1
    * xxx_QA specifies you are connecting to QA server or Dev server using 'True' or 'False', by default it is 'False'
    * IS_PRINTER_CONFIGURED specifies if your Android device is connecting to a printer or not using 'True' or 'False', by default it is 'True'
    * OLD_CART_UI specifies if the cart UI is new design or old design using 'True' or 'False', by default it is 'False'
* See ./*.sh script for how  to setup the run

## Project Directories:
* test_suite: it defines the test cases, it is like your test spec
* actions: it contains all of the ACTIONS, like find an element, scroll and click it.
* labels: it contains the TEXTS in xxx App, say, 'Tax rates will be autoxxx'
* configs: it defines the test configurations, say, which apk you wanted to test
* paths: it defines the PATHS how can you find the elements, say, 'com.xxxpos.th:id/oc_switch_active'
* conftest.py: it defines python fixtures for the test run
* pytest.ini: it configures how pytest runs

## Want to contribute
* Pull a branch from master branch
* Submit a merge request, and provide your .html test result, and assign to Luohua

## When all else fails
* https://luohuahuang.org/2019/02/24/android-client-ui-automation-tips/
* Any questions please contact luohua.huang@gmail.com
