# API requests via Postman
## About / Qwallity app

* Qwallity app is an application where users can register, login to the system, add account balance and make operations with Courses.

In Courses (Fundamental and Advanced) section the admin user can add courses, as well as delete or edit them. Non-admin user can only buy courses.


## Usage

* Signup for Postman Account
* Click New for createing a new collection or environment
* Set HTTP request: e.g. POST
* In the request URL field input API
* Switch to Body tab (if needed)
* In Body click raw, select JSON
* Add data which want to post in JSON format
* Add status checking under Test tab
* Save and click Send
* You will see Status: e.g. 200 OK
* Check Test Result (Pass/Fail)

*Posted data are showing up in the body*

## API Requests Functionality

* Login - *Page is for Login to the system*
* Register User - *User should register to the system with some validations*
* Get advanced course - *This request shows all existing courses in appropriate type*
* Get fundamental course - *This request shows all existing courses in appropriate type*
* Add new course - *User with Admin permission can add course with Fundamental and Advance course types*
* Update course by given course_id - *User with Admin permission can update/edit any existing course*
* Delete course by given course_id - *User with Admin permission can delete any existing course*
* Get User Account Balance - *Users can add amount to theirs account balance*
* Buy Course - *User can buy any course with Funcdamental or Advanced course types*
* Get Course's price by id - *This request allows to get course by it's course_id*
* Get User Role - *This request allows to get user's role*
* Update User Role - *User with Admin permission can update user's role*

## Resources (Documentation and other links) 
* Documentation is available via Swagger private link
* https://www.postman.com
