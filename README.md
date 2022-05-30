# Group_Expense_Tracker
An Appllication created using Python3
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is Group Expense Tracker where we can create a group and after adding all the expenses, It shows the simplified way of paying debts among group members. 
Along with this, you can add, modify or delete expenses as an when needed.
	
## Technologies
Project is created with:
* Python 3.9
* Django 3.1.1
* Django Rest Framework 3.12.4
* Postman
	
## Setup
1. Installation
	* Install Python 3.9 from [Python](https://www.python.org/downloads/).
	* To install Django, open Terminal/Command prompt and run run the following command
	```
	pip install django==3.1.1
	```
	* To install Django Rest Framework, open Terminal/Command prompt and run the following command
	```
	pip install djangorestframework==3.12.4
	```
	* Install Postman from [Postman](https://www.postman.com/downloads/).

2. Download the zip and extract it.
3. Right click in the folder and select *Open in Terminal* and run the following command
```
python manage.py runserver
```
4. You will see something like this.

![new](https://user-images.githubusercontent.com/83489527/171010571-b4823253-a8c7-4571-9915-e9a617296c3f.jpg)

5. Now, Open Postman and select the bottom right cornor icon for better view and click on 'Body' and select **raw** **JSON**. 

![image](https://user-images.githubusercontent.com/83489527/171014376-988fb197-7e49-4876-a6aa-4507e612d442.jpg)

6. Now,

	* To Create Expense, enter the following link in URL and select "POST" response. Now, Enter the group data in the format as shown in the Figure and click on 	       Send.
	```
	http://127.0.0.1:8000/api/create
	
	```
	![Screenshot (56)](https://user-images.githubusercontent.com/83489527/171016804-8187208c-9549-4234-bfa1-0e3bc3ae0b72.png)

	* To Add Expense, enter the following link in URL and select "POST" response. Now, Enter the expense data in the format as shown in the Figure and click on             Send.
	```
	http://127.0.0.1:8000/api/add
	```
	![Screenshot (57)](https://user-images.githubusercontent.com/83489527/171016911-613dbd30-6677-4f17-a4b2-6a47753e6b8c.png)
	
	* To Update Expense, enter the following link in URL and select "PUT" response. Now, Enter the expense data in the format as shown in the Figure and click on           Send.
	```
	http://127.0.0.1:8000/api/update
	```
	![Screenshot (58)](https://user-images.githubusercontent.com/83489527/171017033-1d590153-6a2f-451a-b50c-0fddf019d767.png)
	
	* To Delete Expense, enter the following link in URL and select "DELETE" response. Now, Enter the expense data in the format as shown in the Figure and click           on Send.
	```
	http://127.0.0.1:8000/api/delete
	```
	![Screenshot (59)](https://user-images.githubusercontent.com/83489527/171017233-877cc4c8-e5cb-4573-92fc-bd81e2e1bbc9.png)
	
	* To Get Balance, enter the following link in URL and select "GET" response and then click on Send.
	```
	http://127.0.0.1:8000/api/balance
	```
	![Screenshot (61)](https://user-images.githubusercontent.com/83489527/171017449-229fc2f2-a9d1-4a19-88a1-7e7c00eca824.png)

