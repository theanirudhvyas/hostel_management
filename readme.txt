Hostel Management System       version 1.0      21 March 2016


CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Maintainers

 INTRODUCTION
------------

The hostel management system is a software that will enable the administrative staff to manage the allocation, de-allocation and changing the rooms of students easily. Students can view their allotted rooms, request for a change in their allotted rooms and view various details related to their rooms at a click of a mouse button. 	
The hostel management system aims to reduce the physical effort put in by both the administrative staff and the students in order to achieve the task at their hands related to rooms. As the number of institutions are increasing, so are the number of rooms and hostels in each of the institutes thus increasing the strain on the administrative staff. We aim to reduce the errors that occur when the tasks are manually executed by assignment to the same through an automated computer software. 	
The software is user friendly with an easy to understand and an easy to use Graphics User Interface. The User interface and the webpages have been designed keeping in mind the normal student and staff who are our expected customers on the software. The software helps improve efficiency of running the system by - 
 •Less human error •Strength and strain of manual labour can be reduced •High security •Data redundancy can be avoided to some extent •Data consistency •Easy to handle •Easy data updating •Easy record keeping •Backup data can be easily generated

REQUIREMENTS
------------

This module requires the following modules:

* Python 2.7 
* Django 1.9.4

To run the user interface of the web-app, an internet connection is necessary.

INSTALLATION
------------

* Clone the whole repository to your local machine.
* Open the terminal and change it to the directory of the cloned repo.
* Write the following command -
	python manage.py runserver
* Open the browser and go to your localhost (127.0.0.1:8000/hostel) using the default port number.
* In order to gain the admin rights, run the following command in your terminal - 
	python manage.py createsuperuser

CONFIGURATION
-------------

* To begin with, type in the following url - localhost/hostel/login
* By default this web-app has been configured with the basic databases. Find the below login credentials if you choose to use the default database - 
	
	login id (STUDENT) - asd
	password - asdpassword 

	login id (STUDENT) - 1
	password - 1password

	login id (ADMIN) - qwe
	password - qwepassword

	login id (STUDENT) - qwe1
	password - qwe1password



MAINTAINERS
-----------

Anirudh Vyas : ug201313003@iitj.ac.in
Achyut Joshi : ug201313015@iitj.ac.in
Himanshu Sikaria : ug201314007@iitj.ac.in
Tarun Devireddy : ug201313037@iitj.ac.in

