# Group_Expense_Tracker

## Project Statement
The goal of this project is to create a simple expense tracker in which a group of people can manage their expenses and get a summary of their balance.


## Project Features - 

1. Ability to create a group
	```
	{
          "name": "Home",
          "members": ["A","B"]
        }
	```
	- Each group should have a name and list of members
	- Whenever an expense is added within a group, the members of the expense who are not part of the group should automatically be added as a member.
	  For example - A user creates a group "Home" with members ["A", "B"] and later adds an expense which has user "C", the group members will be - ["A" "B", "C"]
2. Ability to add an expense within a group
	Structure of an expense - 
  
        {
          "name": "Fruits and Milk",
          "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                    {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
        }
3. Ability to update an expense within a group
    - Structure same as add expense.
4. Ability to delete an expense within a group
5. Ability to get the balance of a group such that the balances are simplified. which means -
    - If A,B,C are in a group such that A owes B Rs 100, B owes C Rs 100, the balance summary should show that A owes C Rs 100
    - The structure should be -

    	    {
            "name": "Home",
            "balances": {
              "A": {
                "total_balance": -100.0
                "owes_to": [{"C": 100}],
                "owed_by": []
              },
              "B": {
                "total_balance": 0.0
                "owes_to": [],
                "owed_by": []
              },
              "C": {
                "total_balance": 100.0
                "owes_by": [{"A": 100}],
                "owed_to": []
              }
            }
        	}



## Project Implementation Details -

1. Keep everything in memory. No need to use a database.
2. Create REST API for all the 5 features
3. The code should be clean and object oriented.
4. The system should be consistent always. If multiple people are trying to edit the same bill at the same time, we should take the edits one at at a time and the latest update should be applied. 
	For example - If inital expense is of Rs 100, and A is trying to update the bill to Rs 120, B is trying to update the bill to Rs 80, the system should apply updates sequencially and the balances should be consistent. [Hint - think about locking mechanisms to apply]


## --------------------------------------------------------------------------------------------------------

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

